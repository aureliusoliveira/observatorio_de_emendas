# 🏛️ Observatório de Emendas

**Observatório de Emendas** é uma iniciativa de código aberto que rastreia o caminho das emendas parlamentares federais no Brasil — da origem ao destino final — com o objetivo de fortalecer a transparência pública e o controle social.

> Transparência não é apenas um direito — é uma ferramenta de cidadania e defesa da democracia.

---

## 🎯 Objetivo

Mapear e tornar visível o ciclo completo do gasto público originado por emendas parlamentares:
- Quem indicou a emenda?
- Qual órgão executou?
- Quem recebeu o dinheiro?
- A obra foi concluída?

---

## 📊 O que o projeto oferece

- Coleta automatizada de dados de emendas, empenhos e pagamentos do governo federal.
- Base de dados estruturada com rastreabilidade completa.
- Dashboard interativo (MVP em construção) com filtros por parlamentar, município, tipo de gasto e beneficiário.
- Publicação de análises, achados e padrões suspeitos a partir dos dados.

---

## 📦 Status

🚧 MVP em desenvolvimento – primeira versão do dashboard em breve.  
👥 Projeto mantido por cidadãos comprometidos com o interesse público.  
🌐 Código aberto e colaborativo.

---

## 🚀 Comece agora

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/observatorio-das-emendas.git
cd observatorio-das-emendas
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute a coleta de dados
```bash
python scripts/coletar_emendas.py
```

### 4. Rode o dashboard (exemplo com Streamlit)
```bash
streamlit run app/dashboard.py
```

---

## 🛡️ Sobre o projeto

Este projeto é mantido de forma aberta e transparente por cidadãos preocupados com a boa gestão dos recursos públicos.

Leia o [MANIFESTO](./docs/MANIFESTO.md) para entender os princípios e motivações do Observatório de Emendas.

---

## 🤝 Contribua

- Veja as tarefas abertas no [Project Kanban](https://github.com/users/aureliusoliveira/projects/3).
- Leia o [CONTRIBUTING.md](./docs/CONTRIBUTING.md).
- Participe da comunidade ou envie suas sugestões via GitHub Issues.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).

---

## 📚 Recursos adicionais

- [Fontes de Dados Oficiais](./docs/fontes_de_dados.md) (em construção)

---

> “Só se pode exigir responsabilidade onde há rastreabilidade.”  
> — Observatório das Emendas
