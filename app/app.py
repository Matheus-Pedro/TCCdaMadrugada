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

        sql = 'INSERT INTO Usuario (nome, email, senha, status) VALUES (%s, %s, %s, %s)'
        data = (nome, email, senha, 1)
        mycursor.execute(sql, data)
        mydb.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)