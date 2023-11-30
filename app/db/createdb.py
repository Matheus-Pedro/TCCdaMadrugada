import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    port="3306"
)
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS CAMPUS_CONNECTION_DB')
cursor.execute('USE CAMPUS_CONNECTION_DB')

users_table = """
    CREATE TABLE IF NOT EXISTS Usuario(
        cod_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100),
        senha VARCHAR(100),
        status TINYINT
    )
"""

colleges_table = """
    CREATE TABLE IF NOT EXISTS Universidade(
        cod_universidade INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(240),
        descricao VARCHAR(1000),
        localizacao VARCHAR(255),
        status TINYINT
    )
"""

images_table = """
    CREATE TABLE IF NOT EXISTS Imagem_Universidade(
        cod_imagem INT AUTO_INCREMENT PRIMARY KEY,
        dados_imagem BLOB,
        cod_universidade INT,
        status TINYINT,
        FOREIGN KEY (cod_universidade) REFERENCES Universidade(cod_universidade)
    )
"""

cursor.execute(users_table)
cursor.execute(colleges_table)
cursor.execute(images_table)

cursor.close()
connection.commit()
connection.close()
