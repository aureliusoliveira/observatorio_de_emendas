from abc import ABC, abstractmethod
from typing import Dict
from dotenv import load_dotenv
import os
import ratelimit
import requests
from backoff import on_exception, expo

import logging

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PortalDaTransparenciaAPI(ABC):
    def __init__(self) -> None:
        self.base_endpoint = "https://api.portaldatransparencia.gov.br/api-de-dados"  # TODO: Mover para um arquivo de configuração e pegar o endpoint de lá
        self.headers = {"chave-api-dados": os.getenv("chave-api-dados")}

    @abstractmethod
    def _build_url(self) -> str:
        pass

    @on_exception(expo, ratelimit.exception.RateLimitException, max_tries=10)
    @ratelimit.limits(calls=29, period=30)
    @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    def get_data(self, **params) -> Dict:
        endpoint = self._build_url()
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(url=endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()
