from pymongo import MongoClient
from decouple import config # Variaveis do arquivo .env


# Criando a conexão com MongoDB
client = MongoClient(
    config('MONGO_URL')
)

db = client[f"{config('MONGO_DB')}"]