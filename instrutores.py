import sqlite3

class Instrutores:

    def insert(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        nome = str(input('Nome: '))
        email = int(input('E-mail: '))
        valor_hora = int(input('Valor/Hora: '))
        certificados = str(input("Certificados: "))


        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO instrutores (nome, email, valor_hora, certificados)
        VALUES (?,?,?,?)
        """, (nome, email, valor_hora, certificados))

        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def read(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT id, nome, email FROM instrutores;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def read_id(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
                SELECT * FROM instrutores
                WHERE id = (?)
                """, id)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def update(self, id):
        nome = str(input('Nome: '))
        email = int(input('E-mail: '))
        valor_hora = int(input('Valor/Hora: '))
        certificados = str(input("Certificados: "))

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE instrutores
        SET nome = ?, email = ?, valor_hora = ?, certificados = ?
        WHERE id = ?
        """, (nome, email, valor_hora, certificados, id))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM instrutores
        WHERE id = ?
        """, (id))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()