from portal_da_transparencia.contrato_api import PortalDaTransparenciaAPI

class DespesasPublicasPorOrgaoAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/despesas/por-orgao"

class DespesasPublicasPorFuncionalProgramaticaAPI(PortalDaTransparenciaAPI):
   def _build_url(self) -> str:
       return f"{self.base_endpoint}/despesas/por-funcional-programatica"
