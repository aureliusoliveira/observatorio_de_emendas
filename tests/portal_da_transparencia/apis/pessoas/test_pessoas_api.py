from src.portal_da_transparencia.apis.pessoas.pessoas_api import (
    PessoaFisicaAPI,
    PessoaJuridicaAPI,
)


class TestPessoaFisicaAPI:
    def test_build_url(self) -> str:
        assert (
            PessoaFisicaAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-fisica"
        )


class TestPessoaJuridicaAPI:
    def test_build_url(self) -> str:
        assert (
            PessoaJuridicaAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-juridica"
        )
