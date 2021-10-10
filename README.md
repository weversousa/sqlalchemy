# SQLAlchemy ORM (Object Relational Mapper)

O SQLAlchemy é uma biblioteca do Python que realiza a integração entre as
linguagens Python e um Banco de Dados Relacional.

O ORM é quem permite essa interação acontecer, é como se fosse um interpretador
pois o Pythin não entende SQL e o Banco de Dados Relacional não entende Python.

Para essa interpretação acontecer é necessário ser uma linguagem que aplique OO.

Uma Classe em Python vai representar uma Tabela no Banco de Dados Relacional, e
um Objeto em Python representa uma Tupla (Linha) de um registro de uma Tabale.

## Subqueries

Caso retorne somente 1 Coluna e 1 Linha

    .scalar_subquery()

Para os demais retornos

    .subquery()
