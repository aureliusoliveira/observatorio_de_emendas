from src.portal_da_transparencia.apis.orgaos.orgaos_api import (
    OrgaosSIAPEAPI,
    OrgaosSIAFIAPI,
)


class TestOrgaosSIAPEAPI:
    def test_build_url(self) -> str:
        assert (
            OrgaosSIAPEAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siape"
        )


class TestOrgaosSIAFIAPI:
    def test_build_url(self) -> str:
        assert (
            OrgaosSIAFIAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siafi"
        )
