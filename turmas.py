import sqlite3

class Turmas:

    def insert(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        data_inicio = str(input('Data de Início: '))
        data_final = str(input('Data de Término: '))
        carga_horaria = int(input('Carga Horária: '))

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO turmas (data_inicio, data_final, carga_horaria)
        VALUES (?,?,?)
        """, (data_inicio, data_final, carga_horaria))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def read(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT id, data_inicio, carga_horaria FROM turmas;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def read_id(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM turmas
                WHERE id = (?)
                """, id)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def update(self, id):
        data_inicio = str(input('Data de Início: '))
        data_final = str(input('Data de Término: '))
        carga_horaria = int(input('Carga Horária: '))

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE turmas
        SET data_inicio = ?, data_final = ?, carga_horaria = ?
        WHERE id = ?
        """, (data_inicio, data_final, carga_horaria, id))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM turmas
        WHERE id = ?
        """, (id))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()