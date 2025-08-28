from src.portal_da_transparencia.apis.despesas_publicas.despesas_api import (
    DespesasPublicasPorOrgaoAPI,
    DespesasPublicasPorFuncionalProgramaticaAPI,
)


class TestDespesasPublicasPorOrgaoAPI:
    def test_build_url(self) -> str:
        assert (
            DespesasPublicasPorOrgaoAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/por-orgao"
        )

    def test_get_data_integration_response_ok(self):
        # TODO: É necessáio gerar uma lista ou uma ingestão de órgãos. Ver: https://api.portaldatransparencia.gov.br/swagger-ui/index.html#/%C3%93rg%C3%A3os
        pass


class TestDespesasPublicasPorFuncionalProgramaticaAPI:
    def test_build_url(self) -> str:
        assert (
            DespesasPublicasPorFuncionalProgramaticaAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/por-funcional-programatica"
        )

    def test_get_data_integration_response_ok(self):
        # TODO: É necessáio gerar uma lista ou uma ingestão de órgãos. Ver: https://api.portaldatransparencia.gov.br/swagger-ui/index.html#/%C3%93rg%C3%A3os
        pass
