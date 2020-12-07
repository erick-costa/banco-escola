import sqlite3

class Cursos:

    def insert(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        nome = str(input('Nome: '))
        requisito = str(input('Requisito: '))
        carga_horaria = int(input('Carga Horaria: '))
        preco = float(input('Preço: '))

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO cursos (nome, requisito, carga_horaria, preco)
        VALUES (?,?,?,?)
        """, (nome, requisito, carga_horaria, preco))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def read(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT id, nome, preco FROM cursos;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def read_id(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM cursos
                WHERE id = (?)
                """, id)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def update(self, id):
        nome = str(input('Nome: '))
        requisito = str(input('Requisito: '))
        carga_horaria = int(input('Carga Horaria: '))
        preco = float(input('Preço: '))

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE cursos
        SET nome = ?, requisito = ?, carga_horaria = ?, preco = ?
        WHERE id = ?
        """, (nome, requisito, carga_horaria, preco, id))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM cursos
        WHERE id = ?
        """, (id))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()