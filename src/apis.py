import datetime
from abc import ABC, abstractmethod

import logging
import ratelimit
import requests
from backoff import on_exception, expo

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PortalDaTransparenciaAPI(ABC):

    def __init__(self, path) -> None:
        self.path = path
        self.base_endpoint = "https://api.portaldatransparencia.gov.br/api-de-dados" #TODO: Mover para um arquivo de configuração e pegar o endpoint de lá

    @abstractmethod
    def _get_endpoint(self, **kwargs) -> str:
        pass

    @on_exception(expo, ratelimit.exception.RateLimitException, max_tries=10)
    @ratelimit.limits(calls=29, period=30)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


class EmendasParlamentaresAPI(PortalDaTransparenciaAPI):
    pass
#    path = "emendas"
#
#    def _get_endpoint(self) -> str:
#        return f"{self.base_endpoint}/{self.path}"

class EmendasParlamentaresDocumentosAPI(PortalDaTransparenciaAPI):
    pass
#    type = "emendas/documentos"
#    def __init__(self, code, page):
#        super().__init__()
#
#    def _get_endpoint(self) -> str:
#        return f"{self.base_endpoint}/{self.type}"

class ConveniosDoPoderExecutivoFederalAPI(PortalDaTransparenciaAPI):
    pass

class DespesasPublicasAPI(PortalDaTransparenciaAPI):
    pass
