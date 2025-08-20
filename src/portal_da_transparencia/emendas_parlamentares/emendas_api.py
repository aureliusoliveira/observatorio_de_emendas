from portal_da_transparencia.contrato_api import PortalDaTransparenciaAPI

class EmendasParlamentaresAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/emendas"

class EmendasParlamentaresDocumentosAPI(PortalDaTransparenciaAPI):
   def _build_url(self,  codigo: int=None) -> str:
       return f"{self.base_endpoint}/emendas/documentos/{codigo}"