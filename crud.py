from models import Estado, Cidade
from sqlalchemy import create_engine, or_, func, asc, desc, text, case
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, ProgrammingError

engine = create_engine('sqlite:///mundo.db')

Session = sessionmaker(engine)
session = Session()

# CREATE
try:
    '''
    INSERT INTO estados(nome, uf)
    VALUES ('são paulo', 'sp')
    '''

    estado = Estado(nome='são paulo', uf='sp')

    session.add(estado)
    session.commit()
except IntegrityError:
    session.rollback()


try:
    '''
    INSERT INTO estados(nome, uf)
    VALUES ('bahia', 'ba'),
           ('rio de janeiro', 'rj')
    '''

    list_estados = [
        Estado(nome='bahia', uf='ba'),
        Estado(nome='rio de janeiro', uf='rj')
    ]

    session.add_all(list_estados)
    session.commit()
except IntegrityError:
    session.rollback()

list_cidades = [
    Cidade(nome='osasco', uf='sp', fundacao='1962-02-19'),
    Cidade(nome='salvador', uf='ba', fundacao='1549-03-29'),
    Cidade(nome='florianópolis', uf='sc', fundacao='1673-03-23'),
    Cidade(nome='araçatuba', uf='sp', fundacao='1908-12-02'),
    Cidade(nome='feira de santana', uf='ba', fundacao='1833-09-18'),
    Cidade(nome='brotas', uf='sp', fundacao='1839-05-03'),
    Cidade(nome='belo horizonte', uf='mg', fundacao=None),
    Cidade(nome='brotas', uf='ba', fundacao=None),
]

try:
    session.add_all(list_cidades)
    session.commit()
except IntegrityError:
    session.rollback()

# READ
try:
    '''
    SELECT *
      FROM cidades
    '''

    list_cidade = session.query(Cidade).all()

    for cidade in list_cidade:
        print(cidade.nome, cidade.uf, cidade.fundacao)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
    '''

    list_cidade = session.query(Cidade.nome).all()

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
     LIMIT 4
    '''

    list_cidade = session.query(Cidade.nome).limit(4).all()

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome, uf
      FROM cidades
     WHERE nome = 'brotas'
    '''

    list_cidade = (
        session.query(Cidade.nome, Cidade.uf)
            .filter(Cidade.nome == 'brotas')
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
     WHERE nome = 'brotas'
           AND uf = 'sp'
    '''

    list_cidade = (
        session.query(Cidade.nome, Cidade.uf)
            .filter(Cidade.nome == 'brotas', Cidade.uf == 'sp')
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome, uf
      FROM cidades
     WHERE uf IN('sc', 'mg')
    '''

    list_cidade = (
        session.query(Cidade.nome, Cidade.uf)
            .filter(Cidade.uf.in_(['sc', 'mg']))
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome, uf
      FROM cidades
     WHERE uf = 'sc'
           OR uf = 'mg'
    '''

    list_cidade = (
        session.query(Cidade.nome, Cidade.uf)
            .filter(or_(Cidade.uf == 'sc', Cidade.uf == 'mg'))
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
     WHERE nome LIKE '%santana%'
    '''

    list_cidade = (
        session.query(Cidade.nome)
            .filter(Cidade.nome.like('%santana%'))
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome, fundacao
      FROM cidades
     WHERE fundacao BETWEEN '1800-01-01' AND '1899-12-31'
    '''

    list_cidade = (
        session.query(Cidade.nome, Cidade.fundacao)
            .filter(Cidade.fundacao.between('1800-01-01', '1899-12-31'))
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT uf, COUNT('*') AS 'total_uf'
      FROM cidades
     GROUP BY uf
     ORDER BY total_uf DESC
              uf ASC
    '''

    list_cidade = (
        session.query(Cidade.uf, func.count('*').label('total_uf'))
            .group_by(Cidade.uf)
            .order_by(desc('total_uf'), asc(Cidade.uf))
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT uf, COUNT('*') AS 'total_uf'
      FROM cidades
     GROUP BY uf
    HAVING COUNT('*') > 1
    '''

    list_cidade = (
        session.query(Cidade.uf, func.count('*').label('total_uf'))
            .group_by(Cidade.uf)
            .having(func.count('*') > 1)
            .all()
    )

    for cidade in list_cidade:
        print(cidade)
except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome,
           fundacao,
           DATEDIFF(YEAR, fundacao, GETDATE()) AS 'anos'
      FROM cidades
    '''

except ProgrammingError:
    print('Não foi possível acessar o banco de dados.')
finally:
    print('-' * 80)
