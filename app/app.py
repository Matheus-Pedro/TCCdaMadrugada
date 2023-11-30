from flask import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="db_campus_connection"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def login():
    return render_template('cadastro.html')

<<<<<<< HEAD
@app.route('/cadastro', methods = ['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    sql = 'INSERT INTO Usuario (nome, email, senha, status) VALUES (%s, %s, %s, %s)'
    data = (nome, email, senha, 1)
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount)

    return 'cadastro concluido'
=======
@app.route('/login')
def login():
    return render_template('login.html')
>>>>>>> c1c9159f866971e22b621c8ff8d99a5e2049f155

if __name__ == '__main__':
    app.run(debug=True)