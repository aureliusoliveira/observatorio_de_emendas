from src.portal_da_transparencia.apis.emendas import (
    EmendasParlamentaresAPI,
    EmendasParlamentaresDocumentosAPI,
)


class TestEmendasParlamentaresAPI:
    def test_build_url(self):
        assert (
            EmendasParlamentaresAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/emendas"
        )

    def test_get_data_integration_response_ok(self):
        response = EmendasParlamentaresAPI().get_data(pagina=1)
        assert response[0]["codigoEmenda"] == "201826760002"


class TestEmendasParlamentaresDocumentosAPI:
    def test_build_url(self):
        codigo = 123
        assert (
            EmendasParlamentaresDocumentosAPI()._build_url(codigo)
            == "https://api.portaldatransparencia.gov.br/api-de-dados/emendas/documentos/123"
        )
