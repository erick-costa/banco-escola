import sqlite3

class Alunos:

    def insert(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        cpf = int(input('CPF: '))
        nome = str(input('Nome: '))
        email = str(input('E-mail: '))
        fone = float(input('Telefone: '))
        data_nascimento = str(input('Data de Nascimento: '))

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO alunos (cpf, nome, email, fone, data_nascimento)
        VALUES (?,?,?,?,?)
        """, (cpf, nome, email, fone, data_nascimento))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def read(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT id, nome, email FROM alunos;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def read_id(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM alunos
                WHERE id = (?)
                """, id)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def update(self, id):
        cpf = int(input('CPF: '))
        nome = str(input('Nome: '))
        email = str(input('E-mail: '))
        fone = float(input('Telefone: '))
        data_nascimento = str(input('Data de Nascimento: '))

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE alunos
        SET cpf = ?, nome = ?, email = ?, fone = ?, data_nascimento = ?
        WHERE id = ?
        """, (cpf, nome, email, fone, data_nascimento, id))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM alunos
        WHERE id = ?
        """, (id))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()