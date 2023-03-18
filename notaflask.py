from flask import Flask

app = Flask(__name__)

@app.route('/notas')
def notas():
    nota1 = float(('nota1'))
    nota2 = float(('nota2'))
    media = (nota1 + nota2) / 2

    return media



if __name__ == '__main__':
    app.run(debug=True)