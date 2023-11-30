# IMPORTANTE: LEMBRAR DE CRIAR O BANCO DE DADOS NA MÁQUINA LOCAL PELO ARQUIVO "db/createdb.py". CERTIFIQUE-SE DE INICIALIZAR O SERVIDOR MYSQL COM O XAMP SE NECESSÁRIO.

from flask import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="campus_connection_db"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/get_info_cadastro', methods = ['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        global nome, email, senha
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']

        if senha != confirm_senha:
            return render_template('cadastro.html', mensagem = "As senhas não coincidem.")
        else:
            check_email = f"""
                SELECT * FROM Usuario WHERE email = '{email}'
            """
            mycursor.execute(check_email)
            result = mycursor.fetchall()
            if len(result) > 0:
                return render_template('cadastro.html', mensagem = "Email já cadastrado.")
            else:
                sql = 'INSERT INTO Usuario (nome, email, senha, status) VALUES (%s, %s, %s, %s)'
                data = (nome, email, senha, 1)
                mycursor.execute(sql, data)
                mydb.commit()
                return redirect(url_for('index'))
    
@app.route('/get_info_login', methods=['GET', 'POST'])
def logar_usuario():
    if request.method == 'POST':
        global email, senha
        email = request.form['email']
        senha = request.form['senha']

        consult_user = f"""
            SELECT email, senha FROM Usuario WHERE email = '{email}'
        """
        mycursor.execute(consult_user)
        result = mycursor.fetchall()
        if len(result) > 0:
            senha_bd = result[0][1]
            if senha == senha_bd:
                return redirect(url_for('index'))
            else:
                return render_template('login.html', mensagem = 'Senha incorreta.')

if __name__ == '__main__':
    app.run(debug=True)