# SQLAlchemy ORM (Object Relational Mapper)

O SQLAlchemy é uma biblioteca do Python que realiza a integração entre as
linguagens Python e um Banco de Dados Relacional.

O ORM é quem permite essa interação acontecer, é como se fosse um interpretador
pois o Pythin não entende SQL e o Banco de Dados Relacional não entende Python.

Para essa interpretação acontecer é necessário ser uma linguagem que aplique OO.

Uma Classe em Python vai representar uma Tabela no Banco de Dados Relacional, e
um Objeto em Python representa uma Tupla (Linha) de um registro de uma Tabale.

## Criar uma conexão entre o Python e o Banco de Dados Relacional
```python
# Primeiro precisamos importar a função nessecessária da blioteca SQLAlchemy
from sqlalchemy import create_engine

# Depois nós passamos como parâmetro a string que informa o caminho do Banco
engine = create_engine('sqlite:///nome_do_banco_de_dados.db')

'''
No nosso caso é o SQLite, mas poderia ser qualquer Banco Relacional, exemplos:
    - PostgreSQL
    - MySQL
    - SQL Server...
'''
```

## Criar uma Classe para representar uma Tabela
```python
# Primeiro precisamos importar a função nessecessária da blioteca SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

'''
declarative_base

Retorna uma Classe com todas as configurações necessárias para criar essa
relação, ela  servirá de Herança para as nossas Classes.
'''
Base = declarative_base()


class NomeDaClasse(Base):
    __tablename__ = 'nome da tabela no banco de dados'
    ...
```

Nos arquivos models.py e crud.py que estão nesse repositório eu crio duas
Classes com o mínimo necessário para representar uma Tabela e crio um CRUD
completo para mostar como funciona essa relação de Classe e Objetos entre as
duas linguagens
