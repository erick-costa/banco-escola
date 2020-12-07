import sqlite3
class Matriculas:

    def insert(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        data = str(input('Data de Matrícula: '))

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO matriculas (data_matricula)
        VALUES (?)
        """, (data))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def read(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT id, data_matricula FROM matriculas;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def read_id(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM matriculas
                WHERE id = (?)
                """, id)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def update(self, id):
        data = str(input('Data de Matrícula: '))

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE matriculas
        SET data_matricula = ?
        WHERE id = ?
        """, (data, id))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM matriculas
        WHERE id = ?
        """, (id))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()
