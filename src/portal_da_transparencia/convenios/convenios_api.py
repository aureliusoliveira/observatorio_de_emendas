from portal_da_transparencia.contrato_api import PortalDaTransparenciaAPI

class ConveniosDoPoderExecutivoFederalAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/convenios"

class ConveniosDoPoderExecutivoFederalIdAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/convenios/id"