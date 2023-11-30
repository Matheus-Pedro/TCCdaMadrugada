from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)