from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    # return "Olá, mundo! Aplicação rodando no Docker."
    return render_template('index.html')
    

@app.route('/user/<username>')
def show_user(username):
    return f"Bem-vindo, {username}!"


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run(debug=True)