from sqlalchemy import (
    create_engine, Column, Integer, String, Date, PrimaryKeyConstraint,
    UniqueConstraint, ForeignKeyConstraint, event
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError


engine = create_engine('sqlite:///../database/brasil.db')


@event.listens_for(engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    '''
    Isso aqui é uma dica valiosa...
    O SQLite por padrão desabilitada as funcionalidades de Chave Estrangeira.
    Para saber mais pesquese sobre 'PRAGMAS SQLite'.
    O procedimento abaixo serve para habilitar as funcinalidades.
    (0,) ==> Significa: PRAGMA OFF. Não está habilitado.
    (1,) ==> Significa: PRAGMA ON. Habilitado.
    '''
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')
    cursor.close()


pragma = engine.execute('PRAGMA Foreign_keys;').one()[0]
print('PRAGMA SQLite = ', pragma)


Base = declarative_base()


class Marido(Base):
    __tablename__ = 'marido'
    cpf = Column(String(11))
    nome = Column(String(50), nullable=False)
    esposa_cpf = Column(String(11))
    esposa = relationship(
        argument='Esposa'
    )
    __table_args__ = (
        PrimaryKeyConstraint(cpf, name='pk_marido_cpf'),
        UniqueConstraint(esposa_cpf, name='uq_marido_esposa_cpf'),
        ForeignKeyConstraint(
            [esposa_cpf], ['esposa.cpf'], name='fk_marido_esposa_cpf'
        )

    )

    def __init__(self, cpf, nome, esposa_cpf=None):
        self.cpf = cpf
        self.nome = nome
        self.esposa_cpf = esposa_cpf


class Esposa(Base):
    __tablename__ = 'esposa'
    cpf = Column(String(11))
    nome = Column(String(50), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(cpf, name='pk_esposa_cpf'),
    )

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    try:
        session.add(Esposa(cpf='11111111111', nome='Maria Teixeira'))
        session.commit()
    except IntegrityError:
        session.rollback()
        print('Esse CPF já existe.')

    try:
        # Não vai ser add pois o CPF da Esposa não existe na tabela Esposa
        session.add(
            Marido(
                cpf='22222222222',
                nome='Pedro Teixeira',
                esposa_cpf='33333333333'
            )
        )
        session.commit()
    except IntegrityError:
        session.rollback()
        print('Esse CPF já existe.')
    except:
        print('O CPF da Esposa não existe.')

    try:
        session.add(
            Marido(
                cpf='44444444444',
                nome='Fábio Teixeira',
                esposa_cpf='11111111111'
            )
        )
        session.commit()
    except IntegrityError:
        session.rollback()
        print('Esse CPF já existe. Ou o CPF da Esposa não existe.')

    try:
        # Vai ser add pois o CPF da Esposa poder ser NULL
        session.add(
            Marido(
                cpf='55555555555',
                nome='Carlos Andrade'
            )
        )
        session.commit()
    except IntegrityError:
        session.rollback()
        print('Esse CPF já existe. Ou o CPF da Esposa não existe.')
