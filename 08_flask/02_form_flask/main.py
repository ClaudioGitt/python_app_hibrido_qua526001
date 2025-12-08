from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/enviar")
def enviar():
    # como estamos pegando dados de um formulário, essa é a maneira.
    texto = request.form.get('Texto')
    numero = request.form.get('Numero')
    return render_template("index.html", nome=texto,idade=numero)
if __name__ == "__main__":
    app.run(debug=True)