"""
Executa queries no banco de dados e plota gráficos
"""
import matplotlib.pyplot as plt
from psycopg2 import sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from grupoe.models import City
import pandas as pd

DATABASE = 'grupo_e'
USER = 'postgres'
HOST = 'localhost'
PASSWORD = '123'


def connect_db():
    """
    Conecta no Banco de dados
    :return: Conexão do banco de dados
    """

    engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DATABASE}')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def plot_test():
    session = connect_db()
    cities = session.query(City.city, City.city_ibge_code).filter(City.city_ibge_code==3550308).all()
    cities_df = pd.DataFrame(cities)

    return cities_df


if __name__ == "__main__":
    cities_df = plot_test()
