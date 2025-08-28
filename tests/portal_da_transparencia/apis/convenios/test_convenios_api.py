from src.portal_da_transparencia.apis.convenios.convenios_api import (
    ConveniosDoPoderExecutivoFederalAPI,
    ConveniosDoPoderExecutivoFederalIdAPI,
)


class TestConveniosDoPoderExecutivoFederalAPI:
    def test_build_url(self) -> str:
        assert (
            ConveniosDoPoderExecutivoFederalAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/convenios"
        )

    def test_get_data_integration_response_ok(self):
        response = ConveniosDoPoderExecutivoFederalAPI().get_data(
            pagina=1, dataInicial="21/07/2025", dataFinal="15/08/2025"
        )

        assert "id" in response[0]


class TestConveniosDoPoderExecutivoFederalIdAPI:
    def test_build_url(self) -> str:
        assert (
            ConveniosDoPoderExecutivoFederalIdAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/convenios/id"
        )

    def test_get_data_integration_response_ok(self):
        id = 325659225
        response = ConveniosDoPoderExecutivoFederalIdAPI().get_data(id=id)

        assert response["id"] == 325659225
