from portal_da_transparencia.apis.convenios.convenios import (
    ConveniosDoPoderExecutivoFederalAPI,
    ConveniosDoPoderExecutivoFederalIdAPI,
)
from portal_da_transparencia.apis.despesas import (
    DespesasPublicasPorFuncionalProgramaticaAPI,
    DespesasPublicasPorOrgaoAPI,
)
from portal_da_transparencia.apis.emendas import (
    EmendasParlamentaresAPI,
    EmendasParlamentaresDocumentosAPI,
)
from portal_da_transparencia.apis.pessoas.pessoas import PessoaFisicaAPI, PessoaJuridicaAPI

api = ConveniosDoPoderExecutivoFederalIdAPI()


def main():
    responses = []
    for page in range(1, 2):
        response = api.get_data(pagina=page)
        responses.append(response)
    for convenio in responses:
        print(convenio[0].get("nomeAutor"))


if __name__ == "__main__":
    main()
