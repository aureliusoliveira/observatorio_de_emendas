from src.portal_da_transparencia.apis.orgaos import (
    OrgaosSIAFIAPI,
    OrgaosSIAPEAPI,
)


class TestOrgaosSIAPEAPI:
    def test_build_url(self):
        assert (
            OrgaosSIAPEAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siape"
        )


class TestOrgaosSIAFIAPI:
    def test_build_url(self):
        assert (
            OrgaosSIAFIAPI()._build_url()
            == "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siafi"
        )
