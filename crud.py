from sqlalchemy import func, case
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, OperationalError

from models import Estado, Cidade, engine


# A "session" é quem manipula a "engine", podem ser criadas várias "sessions"
Session = sessionmaker(engine)
session = Session()


# CREATE

try:
    '''
    INSERT INTO estados(nome, uf)
    VALUES ('são paulo', 'sp')
    '''
    session.add(Estado(nome='são paulo', uf='sp'))
    session.commit()
except OperationalError:
    session.rollback()
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
except IntegrityError:
    session.rollback()
    print('Não permitido devido as restriçoes das chaves da tabela.')

try:
    '''
    INSERT INTO estados(nome, uf)
    VALUES ('bahia', 'ba'),
           ('rio de janeiro', 'rj')
    '''
    session.add_all([
        Estado(nome='bahia', uf='ba'),
        Estado(nome='rio de janeiro', uf='rj'),
        Estado(nome='pernambuco', uf='pe'),
    ])
    session.commit()
except OperationalError:
    session.rollback()
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
except IntegrityError:
    session.rollback()
    print('Não permitido devido as restriçoes das chaves da tabela.')

try:
    session.add_all([
        Cidade(nome='osasco', uf='sp', fundacao='1962-02-19'),
        Cidade(nome='olinda', uf='pe', fundacao=None),
        Cidade(nome='salvador', uf='ba', fundacao='1549-03-29'),
        Cidade(nome='florianópolis', uf='sc', fundacao='1673-03-23'),
        Cidade(nome='araçatuba', uf='sp', fundacao='1908-12-02'),
        Cidade(nome='recife', uf='pe', fundacao='1537-03-12'),
        Cidade(nome='feira de santana', uf='ba', fundacao='1833-09-18'),
        Cidade(nome='brotas', uf='sp', fundacao='1839-05-03'),
        Cidade(nome='belo horizonte', uf='mg', fundacao=None),
        Cidade(nome='caruaru', uf='pe', fundacao=None),
        Cidade(nome='petrolina', uf='pe', fundacao=None),
    ])
    session.commit()
except OperationalError:
    session.rollback()
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
except IntegrityError:
    session.rollback()
    print('Não permitido devido as restriçoes das chaves da tabela.')


# READ

try:
    '''
    SELECT *
      FROM cidades
    '''
    list_cidade = session.query(Cidade).all()

    for cidade in list_cidade:
        print(cidade.nome, cidade.uf, cidade.fundacao)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
        .filter((Cidade.uf == 'sc') | (Cidade.uf == 'mg'))
        .all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
     WHERE fundacao IS NULL
    '''
    list_cidade = (
        session.query(Cidade.nome, Cidade.fundacao)
        .filter(Cidade.fundacao.is_(None))
        .all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome
      FROM cidades
     WHERE fundacao IS NOT NULL
    '''
    list_cidade = (
        session.query(Cidade.nome, Cidade.fundacao)
        .filter(Cidade.fundacao.isnot(None))
        .all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT uf, COUNT('*')
      FROM cidades
     GROUP BY uf
     ORDER BY COUNT('*') DESC
              uf ASC
    '''
    list_cidade = (
        session.query(Cidade.uf, func.count('*'))
        .group_by(Cidade.uf)
        .order_by(func.count('*').desc(), Cidade.uf.asc())
        .all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
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
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''--SQL Server
    SELECT DATEDIFF(YEAR, fundacao, GETDATE()) AS 'anos'
      FROM cidades

    session.query(
        func.datediff(text('year'), Cidade.fundacao, func.getdate())
    ).all()
    '''

    '''--SQLite
    SELECT nome,
           fundacao,
           STRFDATE('%Y', DATE('NOW', 'localtime'))
           - STRFDATE('%Y', DATE(fundacao)) AS 'anos'
      FROM cidades
    '''
    list_cidade = (
        session.query(
            Cidade.nome,
            Cidade.fundacao,
            func.STRFTIME('%Y', func.DATE('NOW', 'localtime'))
            - func.STRFTIME('%Y', func.DATE(Cidade.fundacao))
        ).all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT uf,
           CASE
           WHEN uf = 'ba' THEN 'Nordeste'
           WHEN uf = 'sp' THEN 'Sudeste'
           ELSE 'Outro'
           END
    '''
    list_cidade = (
        session.query(
            Cidade.uf,
            case(
                [Cidade.uf == 'ba', 'Nordeste'],
                [Cidade.uf == 'sp', 'Sudeste'],
                else_='Outro'
            )
        ).all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT estados.uf, estados.nome, cidades.nome
      FROM estados
           INNER JOIN cidades
           ON estados.uf = cidades.uf
    '''
    list_estado_join_estado = (
        session.query(Estado.uf, Estado.nome, Cidade.nome)
        .join(Cidade, Estado.uf == Cidade.uf)  # filter(Estado.uf == Cidade.uf)
        .all()
    )

    for estado_join_estado in list_estado_join_estado:
        print(estado_join_estado)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT estados.uf, estados.nome, cidades.nome
      FROM estados
           LEFT JOIN cidades
           ON estados.uf = cidades.uf
    '''
    list_estado_join_estado = (
        session.query(Estado.uf, Estado.nome, Cidade.nome)
        .outerjoin(Cidade, Estado.uf == Cidade.uf)
        .all()
    )

    for estado_join_estado in list_estado_join_estado:
        print(estado_join_estado)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT estados.uf, estados.nome, cidades.nome
      FROM estados
           RIGHT JOIN cidades
           ON estados.uf = cidades.uf
    '''
    list_estado_join_estado = (
        session.query(Estado.uf, Estado.nome, Cidade.nome)
        .outerjoin(Estado, Estado.uf == Cidade.uf)
        .all()
    )

    for estado_join_estado in list_estado_join_estado:
        print(estado_join_estado)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
finally:
    print('-' * 80)

try:
    '''
    SELECT nome, uf
      FROM estados
     WHERE uf = (
                 SELECT uf
                 FROM cidades
                 GROUP BY uf
                 HAVING COUNT('*') > 3
                )
    '''
    list_cidade = (
        session.query(Estado.nome, Estado.uf)
        .filter(Estado.uf == (
                              session.query(Cidade.uf)
                              .group_by(Cidade.uf)
                              .having(func.count('*') > 3)
                              .scalar_subquery()
                              )
                ).all()
    )

    for cidade in list_cidade:
        print(cidade)
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')


# UPDATE

try:
    '''
    UPDATE cidades
       SET 'ribeirão preto'
     WHERE nome = 'araçatuba'
    '''
    list_cidade = (
        session.query(Cidade).filter(Cidade.nome == 'araçatuba').all()
    )

    for cidade in list_cidade:
        cidade.nome = 'ribeirão preto'
        cidade.fundacao = None

    session.commit()
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')


# DELETE

try:
    '''
    DELETE
      FROM cidades
     WHERE id == 1
    '''
    session.delete(session.query(Cidade).get(1))  # get busca pela primary key
    session.commit()
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')

try:
    '''
    DELETE
      FROM cidades
     WHERE nome == 'brotas'
    '''
    session.query(Cidade).filter(Cidade.nome == 'brotas').delete()
    session.commit()
except OperationalError:
    print('Banco e/ou tabela não encontrados. Verificar string de conexão ')
