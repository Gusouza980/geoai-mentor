import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# Load environment variables and save in os.environ
load_dotenv()

# Define the template. This is the prompt that will be used to generate the response.
template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático."), # This is the system prompt.
    ("placeholder", "{historico}"), # This is the placeholder for the history of the conversation.
    ("human", "{query}") # This is the placeholder for the user's query.
])

# Initialize the model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Define the session history.
session_history = {}

session_id = "geoaimentor"

# Define the function that will be used to get the session history.
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_history:
        session_history[session_id] = InMemoryChatMessageHistory()
    return session_history[session_id]


# Define the chain. This is the chain that will be used to generate the response.
chain = RunnableWithMessageHistory(
    runnable=template | model | StrOutputParser(), # This is the chain that will be used to generate the response.
    get_session_history=get_session_history, # This is the function that will be used to get the session history.
    input_messages_key="query", # This is the key for the input messages.
    history_messages_key="historico" # This is the key for the history messages.
)


answers = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]

# Define the loop to answer the questions.
for answer in answers:
    response = chain.invoke(
        input={
            "query": answer
        }, 
        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )
    print(response)