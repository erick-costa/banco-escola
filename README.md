# Banco Escola

> Realiza várias operações em um banco de dados

Este projeto contém um arquivo com banco de dados SQLite, composto por 5 tabelas:
* alunos
* cursos
* instrutores
* matriculas
* turmas

Cada tabela tem um módulo python que a representa, onde contém 4 funções que
realiza 4 operações na tabela:
* Inserção de dados
* Seleção de todos os dados
* Seleção de um registro
* Atualização de um registro
* Exclusão de um registro

Existe um módulo chamado admin, onde o usuário primeiramente seleciona uma tabela
do banco, depois seleciona uma das operações listadas anteriormente. Se a operação
(seleção, atualização ou exclusão de um registro) for uma que necessita de um
dado (id) para localizar um registro no banco, este dado também é requisitado do
usuário.

## Como rodar

```python admin.py```