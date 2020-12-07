from cursos import Cursos
from alunos import Alunos
from instrutores import Instrutores
from matriculas import Matriculas
from turmas import Turmas

print('Administração de Banco de Dados\n')
print('Selecione uma tabela: ')
tabela = int(input('1 - Cursos\n2 - Alunos\n3 - Instrutores\n4 - Turmas\n5 - Matriculas\n'))
print('Selecione uma operacao: ')
operacao = int(input('1 - Inserir dados\n2 - Mostrar tabela\n3 - Mostrar uma linha\n4 - Atualizar\n5 - Excluir\n'))

if tabela == 1:
    if operacao == 1:
        c = Cursos()
        c.insert()
    elif operacao == 2:
        c = Cursos()
        c.read()
    elif operacao == 3:
        id = input('Digite um id: ')
        c = Cursos()
        c.read_id(id)
    elif operacao == 4:
        id = input('Digite um id: ')
        c = Cursos()
        c.update(id)
    elif operacao == 5:
        id = input('Digite um id: ')
        c = Cursos()
        c.delete(id)

elif tabela == 2:
    if operacao == 1:
        c = Alunos()
        c.insert()
    elif operacao == 2:
        c = Alunos()
        c.read()
    elif operacao == 3:
        id = input('Digite um id: ')
        c = Alunos()
        c.read_id(id)
    elif operacao == 4:
        id = input('Digite um id: ')
        c = Alunos()
        c.update(id)
    elif operacao == 5:
        id = input('Digite um id: ')
        c = Alunos()
        c.delete(id)

elif tabela == 3:
    if operacao == 1:
        c = Instrutores()
        c.insert()
    elif operacao == 2:
        c = Instrutores()
        c.read()
    elif operacao == 3:
        id = input('Digite um id: ')
        c = Instrutores()
        c.read_id(id)
    elif operacao == 4:
        id = input('Digite um id: ')
        c = Instrutores()
        c.update(id)
    elif operacao == 5:
        id = input('Digite um id: ')
        c = Instrutores()
        c.delete(id)

elif tabela == 4:
    if operacao == 1:
        c = Turmas()
        c.insert()
    elif operacao == 2:
        c = Turmas()
        c.read()
    elif operacao == 3:
        id = input('Digite um id: ')
        c = Turmas()
        c.read_id(id)
    elif operacao == 4:
        id = input('Digite um id: ')
        c = Turmas()
        c.update(id)
    elif operacao == 5:
        id = input('Digite um id: ')
        c = Turmas()
        c.delete(id)

elif tabela == 5:
    if operacao == 1:
        c = Matriculas()
        c.insert()
    elif operacao == 2:
        c = Matriculas()
        c.read()
    elif operacao == 3:
        id = input('Digite um id: ')
        c = Matriculas()
        c.read_id(id)
    elif operacao == 4:
        id = input('Digite um id: ')
        c = Matriculas()
        c.update(id)
    elif operacao == 5:
        id = input('Digite um id: ')
        c = Matriculas()
        c.delete(id)