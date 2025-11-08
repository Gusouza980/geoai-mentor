# 🌍 GeoAI Mentor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Um assistente inteligente para geocientistas que desejam migrar para a área de Ciência de Dados**

[Sobre](#-sobre) •
[Funcionalidades](#-funcionalidades) •
[Instalação](#-instalação) •
[Como Usar](#-como-usar) •
[Tecnologias](#-tecnologias) •
[Contribuindo](#-contribuindo)

</div>

---

## 📋 Sobre

O **GeoAI Mentor** é um chatbot especializado desenvolvido com LangChain e OpenAI que auxilia profissionais das geociências em sua transição de carreira para a área de Ciência de Dados. O assistente oferece orientações personalizadas, sugestões de aprendizado e conselhos práticos baseados em conversas contextualizadas.

### 🎯 Objetivo

Facilitar a jornada de aprendizado de geocientistas (geólogos, geofísicos, geógrafos, etc.) que buscam expandir suas habilidades para o campo de Data Science, Machine Learning e Inteligência Artificial.

---

## ✨ Funcionalidades

- 🤖 **Assistente Conversacional Inteligente**: Utiliza GPT-3.5-turbo para respostas contextualizadas
- 💬 **Memória de Conversação**: Mantém o histórico da conversa para respostas mais coerentes
- 🎓 **Foco em Geociências**: Especializado em orientar geocientistas na transição de carreira
- 📚 **Orientações Personalizadas**: Sugestões de linguagens, projetos e caminhos de aprendizado
- 🔄 **Didático e Amigável**: Tom de conversa acessível e educativo

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com API Key ([Obtenha aqui](https://platform.openai.com/api-keys))

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/geoai-mentor.git
cd geoai-mentor
```

2. **Crie um ambiente virtual** (recomendado)

```bash
# No Linux/Mac
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_api_aqui
```

> ⚠️ **Importante**: Nunca compartilhe sua chave API publicamente ou a inclua no controle de versão!

---

## 💻 Como Usar

### Execução Básica

```bash
python chatbot_mentory.py
```

### Personalização

Você pode modificar as perguntas no arquivo `chatbot_mentory.py`:

```python
answers = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]
```

### Exemplo de Saída

```
Olá! Para um geofísico interessado em migrar para ciência de dados, recomendo começar 
com Python. É a linguagem mais popular na área, possui excelentes bibliotecas como 
Pandas, NumPy e Scikit-learn, além de ser amplamente usada em geociências...

Excelente pergunta! Você poderia criar um projeto analisando dados sísmicos, 
desenvolvendo modelos de predição de reservatórios, ou até mesmo criando 
visualizações interativas de dados geoespaciais...
```

---

## 🛠️ Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

| Tecnologia | Descrição |
|------------|-----------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Linguagem de programação |
| ![LangChain](https://img.shields.io/badge/🦜_LangChain-2E8B57?style=flat) | Framework para desenvolvimento com LLMs |
| ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white) | API de IA (GPT-3.5-turbo) |
| ![dotenv](https://img.shields.io/badge/.env-ECD53F?style=flat&logo=dotenv&logoColor=black) | Gerenciamento de variáveis de ambiente |

### Dependências Principais

```
langchain-openai     # Integração LangChain com OpenAI
langchain-core       # Componentes core do LangChain
python-dotenv        # Carregamento de variáveis de ambiente
openai               # SDK oficial da OpenAI
```

---

## 📁 Estrutura do Projeto

```
geoai-mentor/
│
├── chatbot_mentory.py    # Script principal do chatbot
├── requirements.txt      # Dependências do projeto
├── .env.example         # Exemplo de configuração
├── .env                 # Configuração (não versionado)
└── README.md            # Este arquivo
```

---

## 🎨 Arquitetura

O projeto utiliza o framework LangChain com os seguintes componentes:

```
┌─────────────────┐
│  User Query     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Chat Template   │ ◄── System Prompt + Histórico
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ OpenAI Model    │ ◄── GPT-3.5-turbo
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Output Parser   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Response      │
└─────────────────┘
```

---

## 🧪 Melhorias Futuras

- [ ] Interface web com Streamlit ou Gradio
- [ ] Suporte a múltiplas sessões de usuários
- [ ] Persistência de histórico em banco de dados
- [ ] Integração com documentação e recursos de aprendizado
- [ ] Sistema de recomendação de cursos
- [ ] Análise de perfil do usuário

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Gustavo**

Desenvolvido durante o curso de Especialista em IA na Alura.

---

## 📧 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato!

---

<div align="center">

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐

Feito com ❤️ e ☕

</div>

