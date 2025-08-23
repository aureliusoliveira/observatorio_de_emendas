# test_writer.py
import json
import pytest

from src.utils.writers import JSONWriter, DataTypeNotSupported  # ajuste o caminho se necessário

@pytest.fixture
def json_writer(tmp_path):
    outpath = tmp_path / "out.jsonl"
    writer = JSONWriter(filepath=str(outpath))
    return writer, outpath


def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def test_jsonwriter_write_single_dict_creates_one_ndjson_line(json_writer):
    writer, outpath = json_writer

    row = {"id": 1, "name": "Alice"}
    writer.write(row)

    assert outpath.exists()
    lines = read_lines(outpath)
    assert len(lines) == 1

    # A linha deve ser um JSON válido equivalente ao dict
    assert json.loads(lines[0]) == row


def test_jsonwriter_write_list_of_dicts_appends_lines(json_writer):
    writer, outpath = json_writer

    data = [{"id": 1}, {"id": 2}, {"id": 3}]
    writer.write(data)

    # Chama novamente para verificar que abre em 'append' e não sobrescreve
    writer.write({"id": 4})

    lines = read_lines(outpath)
    assert len(lines) == 4
    assert [json.loads(l)["id"] for l in lines] == [1, 2, 3, 4]


def test_jsonwriter_write_unsupported_type_raises(json_writer):
    writer, outpath = json_writer

    with pytest.raises(DataTypeNotSupported) as excinfo:
        writer.write("not a dict nor list")

    # Mensagem deve mencionar o tipo inválido
    msg = str(excinfo.value)
    assert "str" in msg
    assert "is not supported for ingestion" in msg
    assert not outpath.exists()  # nada foi criado


def test_jsonwriter_list_with_invalid_element_raises_and_partial_write(json_writer):
    """
    Garante que se a lista contiver um elemento inválido, a exceção é levantada.
    Nota: com a implementação atual (recursiva), itens válidos anteriores já terão sido gravados.
    Este teste documenta esse comportamento.
    """
    writer, outpath = json_writer

    mixed = [{"ok": 1}, 42, {"ok": 3}]
    with pytest.raises(DataTypeNotSupported) as excinfo:
        writer.write(mixed)

    assert "int" in str(excinfo.value)

    # O primeiro elemento válido foi gravado antes de falhar no elemento inválido
    assert outpath.exists()
    lines = read_lines(outpath)
    assert len(lines) == 1
    assert json.loads(lines[0]) == {"ok": 1}


def test_jsonwriter_is_ndjson_1_obj_per_line(tmp_path):
    outpath = tmp_path / "out.jsonl"
    w = JSONWriter(filepath=str(outpath))

    objs = [{"a": i} for i in range(5)]
    w.write(objs)

    with open(outpath, "rb") as f:
        raw = f.read()

    # Deve terminar com \n e ter 5 quebras de linha (uma por objeto)
    assert raw.endswith(b"\n")
    assert raw.count(b"\n") == 5
