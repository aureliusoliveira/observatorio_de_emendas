from portal_da_transparencia.despesas_publicas.despesas_api import \
                                                    DespesasPublicasPorOrgaoAPI,\
                                                    DespesasPublicasPorFuncionalProgramaticaAPI

class TestDespesasPublicasPorOrgaoAPI:
    def test_build_url(self) -> str:
        assert DespesasPublicasPorOrgaoAPI()._build_url() == \
            "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/por-orgao"

class TestDespesasPublicasPorFuncionalProgramaticaAPI:
    def test_build_url(self) -> str:
        assert DespesasPublicasPorFuncionalProgramaticaAPI()._build_url() == \
            "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/por-funcional-programatica"