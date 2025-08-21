from ..contrato_api import PortalDaTransparenciaAPI

class PessoaFisicaAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/pessoa-fisica"

class PessoaJuridicaAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/pessoa-juridica"
