import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306"
)
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS CAMPUS_CONNECTION_DB')
cursor.execute('USE CAMPUS_CONNECTION_DB')

users_table = """
    CREATE TABLE IF NOT EXISTS USUARIOS(
        COD_USUARIO INT AUTO_INCREMENT PRIMARY KEY,
        NOME VARCHAR(100),
        EMAIL VARCHAR(100),
        SENHA VARCHAR(100),
        STATUS TINYINT
    )
"""

colleges_table = """
    CREATE TABLE IF NOT EXISTS UNIVERSIDADES(
        COD_UNIVERSIDADE INT AUTO_INCREMENT PRIMARY KEY,
        NOME VARCHAR(240),
        DESCRICAO VARCHAR(1000),
        LOCALIZACAO VARCHAR(255)
    )
"""

images_table = """
    CREATE TABLE IF NOT EXISTS IMAGENS_UNIVERSIDADE(
        COD_IMAGEM INT AUTO_INCREMENT PRIMARY KEY,
        DADOS_IMAGEM BLOB,
        COD_UNIVERSIDADE INT,
        STATUS TINYINT,
        FOREIGN KEY (COD_UNIVERSIDADE) REFERENCES UNIVERSIDADES(COD_UNIVERSIDADE)
    )
"""

cursor.execute(users_table)
cursor.execute(colleges_table)
cursor.execute(images_table)

cursor.close()
connection.commit()
connection.close()