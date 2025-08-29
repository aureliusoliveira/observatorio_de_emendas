from .api_interface import PortalDaTransparenciaAPI


class OrgaosSIAPEAPI(PortalDaTransparenciaAPI):
    def _build_url(self) -> str:
        return f"{self.base_endpoint}/orgaos-siape"


class OrgaosSIAFIAPI(PortalDaTransparenciaAPI):
    def _build_url(self) -> str:
        return f"{self.base_endpoint}/orgaos-siafi"
