from src.portal_da_transparencia.apis.convenios.convenios_api \
    import \
        ConveniosDoPoderExecutivoFederalAPI,\
        ConveniosDoPoderExecutivoFederalIdAPI
from src.portal_da_transparencia.apis.despesas_publicas.despesas_api \
    import \
        DespesasPublicasPorFuncionalProgramaticaAPI,\
        DespesasPublicasPorOrgaoAPI
from src.portal_da_transparencia.apis.emendas_parlamentares.emendas_api \
    import \
        EmendasParlamentaresAPI,\
        EmendasParlamentaresDocumentosAPI
from src.portal_da_transparencia.apis.pessoas.pessoas_api \
    import \
        PessoaFisicaAPI,\
        PessoaJuridicaAPI




api = EmendasParlamentaresAPI()

def main():
    responses = []
    for page in range(1,2):
        response = api.get_data(pagina=page)
        responses.append(response)
    for emenda in responses:
        print(emenda[0].get('nomeAutor'))


if __name__ == "__main__":
    main()
