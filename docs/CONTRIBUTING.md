# Guia de Contribuição

Obrigado por considerar contribuir para o **Observatório de Emendas**!  
Este documento explica como instalar o projeto localmente, abrir issues, propor melhorias e enviar Pull Requests (PRs).

---

## 🎯 Objetivo do projeto
Promover transparência e análise de emendas parlamentares, com foco em qualidade de dados, reprodutibilidade e ética.

---

## 🚀 Stack de desenvolvimento
- **Linguagem**: Python (3.11+ recomendado)
- **Gerenciador de dependências**: [uv](https://docs.astral.sh/uv/)
- **Testes**: [pytest](https://docs.pytest.org/)
- **Versionamento**: Git + GitHub

> **Nota:** todo o código deve estar em **inglês** (conforme as diretrizes do projeto).
  
---

## 🧰 Preparando o ambiente (com `uv`)

1) **Clone o repositório**  
```bash
git clone https://github.com/aureliusoliveira/observatorio_de_emendas.git
cd observatorio_de_emendas

```

2) **Instale as dependências** (modo isolado por virtualenv gerenciado pelo `uv`):  
```bash
uv sync
```

3) **Ative o ambiente e execute o projeto/testes**:  
```bash
# Executar qualquer comando no ambiente virtual:
uv run python -V

# Rodar a suíte de testes:
uv run pytest -q
```

4) **Adicionar novas dependências**:  
```bash
# Dependência de runtime
uv add <pacote>

# Dependência de desenvolvimento (ex.: linters, formatadores, libs de teste)
uv add --dev <pacote>

# Atualizar o lockfile
uv lock
```

> Se o projeto usar ferramentas como **ruff** (lint), **black** (format) ou **mypy** (type check), rode-as via `uv run` (ex.: `uv run ruff check .`).

---

## 🧑‍💻 Como contribuir

### 1) Abrindo uma issue
- Use a aba **Issues** no GitHub.
- Preencha um título claro e descreva:
  - Contexto / motivação
  - Passos para reproduzir (se bug)
  - Resultado esperado vs. observado
  - Evidências (prints, logs, amostras de dados anonimizadas)
- Marque com os rótulos (labels) apropriados: `bug`, `enhancement`, `question`, `docs`, etc.

### 2) Propondo uma mudança (Pull Request)
1. **Fork** do repositório e **crie uma branch** descritiva:
   ```bash
   git checkout -b feat/<resumo-curto>
   # ou fix/<resumo-curto>, docs/<resumo-curto>, chore/<resumo-curto>, refactor/<resumo-curto>
   ```
2. **Implemente pequenos commits** e utilize mensagens no formato _Conventional Commits_ quando possível, por exemplo:
   - `feat: add committee aggregation step`
   - `fix: handle missing sponsor id`
   - `docs: update contributing guide`
3. **Garanta qualidade antes do PR**:
   - `uv run pytest -q` sem falhas.
   - (Opcional) `uv run ruff check .` e `uv run ruff format .` ou ferramentas equivalentes.
   - Cobertura de testes para casos relevantes.
4. **Abra o PR** descrevendo o problema, a solução e impactos (performance, schema, compatibilidade).  
   Inclua _checklist_ no corpo do PR:
   - [ ] Incluí testes ou atualizei os existentes
   - [ ] Atualizei a documentação (README/CHANGELOG) quando necessário
   - [ ] Verifiquei performance e compatibilidade
   - [ ] Não inclui dados sensíveis

5. **Responda ao review** com calma e objetividade. Sugestões de melhoria são bem-vindas.

---

## 🔎 Padrões de código & organização
- Siga **PEP 8** e boas práticas de legibilidade.
- Prefira nomes explícitos, funções puras e baixo acoplamento.
- Mantenha utilitários compartilhados em módulos `utils/` quando fizer sentido.
- Para dados de exemplo, use **amostras pequenas anonimizadas** colocadas em `examples/` ou `tests/fixtures/` (evite dados pessoais e sensíveis).

---

## 🧪 Testes (pytest)
- Testes devem ser **determinísticos**, rápidos e com _fixtures_ claras.
- Estruture por módulo/componente (ex.: `tests/<pacote>/test_<arquivo>.py`).
- Dê nomes descritivos aos testes (ex.: `test_should_merge_rows_when_keys_match`).
- Use `pytest -k` para filtrar testes e `-q` para saída concisa.
- Utilize _mocks_ quando integrar com serviços externos.
  
Comandos úteis:
```bash
# Rodar todos os testes
uv run pytest -q

# Rodar um arquivo específico
uv run pytest tests/path/to/test_file.py -q

# Mostrar falhas verbosas
uv run pytest -vv
```

---

## 🔐 Ética, dados e segurança
- **Não inclua dados pessoais/sensíveis** em commits, issues ou PRs.
- Documente a origem de dados públicos e licenças associadas.
- Siga as leis e políticas de uso das fontes de dados.
- Se identificar vulnerabilidade de segurança ou privacidade, **não abra issue pública**. Use o contato privado indicado no `CODE_OF_CONDUCT.md` (seção *Aplicação*).

---

## 📜 Licença
Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do repositório (veja `LICENSE`).

---

## 🙌 Agradecimentos
Obrigado por ajudar a fortalecer a transparência pública com software aberto e de qualidade!
