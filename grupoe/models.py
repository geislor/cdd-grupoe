from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'

    city_ibge_code = Column(Integer, primary_key=True)
    city = Column(String)
    state = Column(String)
    estimated_population_2019 = Column(Integer)

    def __repr__(self):
        return f'City {self.city}'


class Cases(Base):
    __tablename__ = 'cases'

    city_ibge_code = Column(Integer,
           ForeignKey('city.city_ibge_code', ondelete="SET NULL"),
           index=True, primary_key=True)
    city_ibge = relationship(City)

    date = Column(String, primary_key=True)
    epidemiological_week = Column(Integer)
    last_available_confirmed = Column(Integer)
    last_available_deaths = Column(Integer)
    last_available_death_rate = Column(Numeric)
    last_available_confirmed_per_100k_inhabitants = Column(Numeric)

    def __repr__(self):
        return f'IBGE {self.city_ibge_code}, Date {self.date}'
