from abc import ABC, abstractmethod
from typing import Dict
from dotenv import load_dotenv
import os

import logging
import requests

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PortalDaTransparenciaAPI(ABC):
    def __init__(self) -> None:
        self.base_endpoint = "https://api.portaldatransparencia.gov.br/api-de-dados" #TODO: Mover para um arquivo de configuração e pegar o endpoint de lá
        self.headers = {'chave-api-dados': os.getenv('chave-api-dados')}    

    @abstractmethod
    def _build_url(self) -> str:
        pass

    def get_data(self, **params) -> Dict:
        endpoint = self._build_url()
        logger.info(f"Getting data from endpoint: {endpoint}")
        response = requests.get(url=endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()
