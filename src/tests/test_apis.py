from src.apis import EmendasParlamentaresAPI

class TestEmendasParlamentaresAPI:
    def test_build_url(self):
        path = "emendas"
        assert EmendasParlamentaresAPI(path)._build_url() == \
            "https://api.portaldatransparencia.gov.br/api-de-dados/emendas"
        
    