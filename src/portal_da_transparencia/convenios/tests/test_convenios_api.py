from ..convenios_api import ConveniosDoPoderExecutivoFederalAPI, ConveniosDoPoderExecutivoFederalIdAPI
      
class TestConveniosDoPoderExecutivoFederalAPI:
    def test_build_url(self) -> str:
        assert ConveniosDoPoderExecutivoFederalAPI()._build_url() == \
            "https://api.portaldatransparencia.gov.br/api-de-dados/convenios"

class TestConveniosDoPoderExecutivoFederalIdAPI:
    def test_build_url(self) -> str:
        assert ConveniosDoPoderExecutivoFederalIdAPI()._build_url() == \
            "https://api.portaldatransparencia.gov.br/api-de-dados/convenios/id"