"""
Executa queries no banco de dados e plota gráficos
"""
import pandas as pd
import psycopg2
from psycopg2 import sql

DATABASE = 'grupo_e'
USER = 'postgres'
HOST = 'localhost'
PASSWORD = '123'


def connect_db():
    """
    Conecta no Banco de dados
    :return: Conexão do banco de dados
    """

    con = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        host=HOST,
        password=PASSWORD)
    return con


def search(query):
    db = connect_db()
    cur = db.cursor()
    cur.execute(sql.SQL(query))
    return cur.fetchall()


if __name__ == "__main__":
    query = "SELECT * from city;"

    response = search(query)
