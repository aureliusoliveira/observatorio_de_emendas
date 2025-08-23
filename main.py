from src.portal_da_transparencia.emendas_parlamentares.emendas_api import EmendasParlamentaresAPI


api = EmendasParlamentaresAPI()

def main():
    responses = []
    for page in range(1,3):
        response = api.get_data(pagina=page)
        responses.append(response)
        print(responses)


if __name__ == "__main__":
    main()
