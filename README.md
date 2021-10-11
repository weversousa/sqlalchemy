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

## Modelo Relacional
Muitas vezes de inicío para algo difícil de entender, mas não é algo muito
simples. Criar relacionamento entre tabelas é realizar troca de chaves entre
elas. Quando uma tabela recebe uma chave primária de outra tabela, essa chave
recebida é chamada de chave estrangeira.

**Chave Primária** é uma restrição para que o valor seja único na tupla.  
**Chave Estrangeira** é a Chave Primária de outra tabela.


### Relacionamento UM PARA UM
Nós escolhemos qualquer uma das duas tabelas para ser a Dominante, essa tabela
é quem vai receber a Chave Prímária da outra tabela, para ser a sua
Chave Estrangeira.<br>

Um registro da tabela A está ligado somente a um ou nenhum registro da tabela B
Um registro da tabela B está ligado somente a um ou nenhum registro da tabela A<br>

Para garantir essa regra nós devemos acrescentar uma restrição UNIQUE ao campo
que será a Chave Estrangeira, para que ele não possa ser associado a dois
valores.

### Relacionamento UM PARA MUITOS ou MUITOS PARA UM
Nós pegamos a Chave Primária da tabela UM e colocamos ela como
Chave Estrangeira na tabela DOIS

### Relacionamento MUITOS PARA MUITOS
Nesse caso o relacionamento entre duas tabelas vira uma nova Tabela.
Vanos supoer que temos a Tabela A e Tabela B.
Essa nova tabela vai ter a sua prória Chave Primária, e ela vai ter duas
Chaves Estrangeiras, que vão ser a Chave Primária das Tabelas A e B.
