import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="db_campus_connection"
)

mycursor = mydb.cursor()

# ----------- CRUD do Usuario ----------- #


def criar_usuario(usuario):
    sql = 'INSERT INTO Usuario (nome, email, senha, status) VALUES (%s, %s, %s, %s)'
    data = (usuario.nome, usuario.email, usuario.senha, 1)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount)


def editar_nome_usuario(usuario):
    sql = 'UPDATE Usuario SET nome = "%s" WHERE (cod_usuario = %s)'
    data = (usuario.nome, usuario.cod_usuario)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount)


def editar_senha_usuario(usuario):
    sql = 'UPDATE Usuario SET senha = "%s" WHERE (cod_usuario = %s)'
    data = (usuario.senha, usuario.cod_usuario)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount)


def editar_email_usuario(usuario):
    sql = 'UPDATE Usuario SET email = "%s" WHERE (cod_usuario = %s)'
    data = (usuario.email, usuario.cod_usuario)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount)


def deletar_usuario(cod_usuario):
    sql = 'UPDATE Usuario SET nome="", email = "", senha = "", status = 0 WHERE (cod_usuario = %s)'
    mycursor.execute(sql, cod_usuario)
    mydb.commit()
    print(mycursor.rowcount)


def ler_usuario(cod_usuario):
    sql = f'SELECT * FROM Usuario WHERE status = 1 AND cod_usuario = %s'
    mycursor.execute(sql, cod_usuario)
    result = mycursor.fetchone()
    print(result)
    return result


# ----------- CRUD da Imagem Universidade ----------- #

# def criar_imagem_universidade(imagem_universidade):


# ----------- CRUD da Universidade ----------- #
#
# def criar_universidade(universidade):
#     sql = 'INSERT INTO Universidade (nome, descricao, ima, status) VALUES (%s, %s, %s, %s)'
#     data = (usuario.nome, usuario.email, usuario.senha, 1)
#     mycursor.execute(sql, data)
#     mydb.commit()?
