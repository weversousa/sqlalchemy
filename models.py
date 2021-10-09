from datetime import datetime

from sqlalchemy import (
    create_engine, Column, Integer, String, Date, PrimaryKeyConstraint,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///brasil.db')

Base = declarative_base()


class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer)
    nome = Column(String(20), nullable=False)
    uf = Column(String(2), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(id, name='pk_estados_id'),
        UniqueConstraint(nome, name='uq_estados_nome'),
        UniqueConstraint(uf, name='uq_estados_uf'),
    )

    def __init__(self, nome, uf):
        self.nome = nome
        self.uf = uf


class Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer)
    nome = Column(String(20), nullable=False)
    uf = Column(String(2), nullable=False)
    fundacao = Column(Date)
    __table_args__ = (
        PrimaryKeyConstraint(id, name='pk_continentes_id'),
        UniqueConstraint(nome, uf, name='uq_continentes_nome_uf')
    )

    def __init__(self, nome, uf, fundacao):
        self.nome = nome
        self.uf = uf
        self.fundacao = self.set_fundacao(fundacao)

    def set_fundacao(self, fundacao):
        if fundacao:
            return datetime.strptime(fundacao, '%Y-%m-%d')
        return fundacao

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
