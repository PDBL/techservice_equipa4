import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "162.240.171.8"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "Techservice"),
        password=os.getenv("DB_PASSWORD", "TechService@2026!"),
        database=os.getenv("DB_NAME", "techservice_equipa4")
    )