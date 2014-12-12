import config as conf

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key = True)
    user = Column(String) # Saves a hashed twitter user ID
    text = Column(Text)
    search_term = Column(Text) # Saves the search term
    created_at = Column(DateTime)

    def __repr__(self):
        return id


def main():
    '''Crea tablas en la base de datos'''
    
    engine = create_engine(conf.DB_STRING)
    Base.metadata.create_all(engine)
    return "Esquema creado"


if __name__ == '__main__':
    print(main())

