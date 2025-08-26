## Bases essenciais para fiscalização de emendas

### Portal da Transparência – Emendas, despesas e convênios

- **Base URL:** `https://api.portaldatransparencia.gov.br/api-de-dados`
- **Emendas parlamentares:** endpoint `emendas` retorna emendas por ano, código do autor, órgão, etc. Os documentos de cada emenda são obtidos em `emendas/documentos/{codigo}`.
- **Convênios:** a API de convênios permite filtrar por número, número de processo ou código; os principais endpoints são `/convenios`, `/convenios/{id}` e `/convenios/numero-processo`.
- **Despesas:** para examinar execução das emendas nos órgãos e funções de governo, use `/despesas/por-orgao` e `/despesas/por-funcional-programatica`.
- **Pessoas:** informações sobre CPF (`/pessoa-fisica`) e CNPJ (`/pessoa-juridica`).
- **Órgãos:** consulta de órgaos cadastrados no Sistema Integrado de Administração de Pessoal (SIAPE)(`orgaos-siape`) e no Sistema Integrado de Administração Financeira do Governo Federal (SIAFI)(`orgaos-siafi`).
- **Requisito de chave:** esses endpoints exigem cadastro de chave de API gratuita. Sem a chave, apenas a lista de endpoints via Swagger fica acessível; os dados não são retornados.

### SIOP – Emendas Individuais Impositivas

- **Base URL:** `https://siop.planejamento.gov.br/`
- **Endpoints:** a página de documentação indica que as emendas impositivas são acessadas por meio de `/modulo/emendas/api`, `/modulo/itens/api`, `/modulo/impedimentos/api`, `/modulo/qualitativo/api` e `/modulo/quantitativo/classificadores/api`.
- **Observação:** a API está em produção e requer token associado a pessoa física. Não consegui testar sem a credencial.

### Transferegov (Plataforma +Brasil) – Transferências de emendas

- **Base API:** `https://api.transferegov.gestao.gov.br`
- **Módulo “transferenciasespeciais”:** dedica‑se aos repasses de emendas individuais para estados/municípios criados pela Emenda Constitucional 105; inclui endpoints como `/programa_especial`, `/plano_acao_especial`, `/empenho_especial`, entre outros.
- **Módulo “fundoafundo”:** contém transferências fundo a fundo (por exemplo, saúde e assistência social) – endpoints `/programa` e `/programa_beneficiario`.
- **Módulo “ted” (Termo de Execução Descentralizada):** traz dados sobre convênios executados via TED e inclui endpoints `/programa`, `/programa_beneficiario` e `/programa_acao_orcamentaria`.
- **Observação:** esses módulos usam PostgREST; a autenticação via chave de API pode ser requerida dependendo do volume de consultas, mas é possível testar sem token em alguns casos.

 ### Câmara dos Deputados – Dados legislativos

- **Base URL:** `https://dadosabertos.camara.leg.br/api/v2/`
- **Função:** disponibiliza informações de deputados, proposições, discursos e despesas. Não existe endpoint específico para emendas, mas os dados de parlamentares (código, nome, partido) são úteis para cruzar com autores das emendas.

### Senado Federal – Dados abertos

- **Base URL:** `https://legis.senado.leg.br/dadosabertos/`
- **Endpoints:** são divididos por serviços; por exemplo, `agendareuniao/{data}.json` fornece agendas de comissões e `dados/ListaTiposAutor.xml` lista tipos de autor de proposições. Os dados podem ser retornados em JSON ou XML. Não há um serviço específico para emendas parlamentares; usa‑se para complementar dados de senadores.

### IBGE – Localidades

- **Base API:** `https://servicodados.ibge.gov.br/api/v1/localidades`
- **Endpoints:** `estados` e `municipios` retornam códigos e nomes oficiais. Útil para validar municípios beneficiados por emendas.
