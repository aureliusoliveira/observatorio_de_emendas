from portal_da_transparencia.emendas_parlamentares.emendas_api import \
                                                    EmendasParlamentaresAPI,\
                                                    EmendasParlamentaresDocumentosAPI

class TestEmendasParlamentaresAPI:
    def test_build_url(self):
        assert EmendasParlamentaresAPI()._build_url() == 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas'

class TestEmendasParlamentaresDocumentosAPI:
    def test_build_url(self):
        codigo = 123
        assert EmendasParlamentaresDocumentosAPI()._build_url(codigo) == 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas/documentos/123'