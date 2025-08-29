from src.portal_da_transparencia.apis.pessoas import (
    PessoaFisicaAPI,
    PessoaJuridicaAPI,
)


class TestPessoaFisicaAPI:
    def test_build_url(self):
        assert (
            PessoaFisicaAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-fisica"
        )


class TestPessoaJuridicaAPI:
    def test_build_url(self):
        assert (
            PessoaJuridicaAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/pessoa-juridica"
        )
