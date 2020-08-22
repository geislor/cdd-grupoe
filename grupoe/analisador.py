"""
Executa queries no banco de dados e plota gráficos
"""
import pandas as pd
import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt


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


def plot_test():
    query = "SELECT cases.last_available_deaths from cases;"
    response = search(query)
    dataframe = pd.DataFrame(response)
    return dataframe


if __name__ == "__main__":
    dataframe = plot_test()
    pass
