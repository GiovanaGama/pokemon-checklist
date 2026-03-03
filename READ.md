# 🧩 Pokémon TCG Excel Generator

Aplicação web construída com **FastAPI** que permite buscar cartas do Pokémon TCG usando a API do TCGdex e gerar automaticamente um arquivo Excel contendo:

- 🖼️ Ilustração da carta (recortada automaticamente)
- 📛 Nome
- 🔢 Número da carta (localId/total do set)
- 📦 Nome da coleção
- 🔎 Filtros personalizados (illustrator, set, series, name)

---

## 🚀 Tecnologias utilizadas

- FastAPI
- TCGdex SDK
- aiohttp
- openpyxl
- Pillow
- Jinja2

---

## 📸 Como funciona

1. O usuário escolhe um tipo de filtro:
   - illustrator
   - set
   - series
   - name

2. O sistema consulta a API do TCGdex
3. Baixa as imagens das cartas
4. Recorta automaticamente apenas a arte
5. Gera um arquivo Excel em memória
6. Retorna o download para o usuário

---

## 🛠️ Instalação local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo