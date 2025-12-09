from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/enviar", methods=["POST"])
def enviar():
    # como estamos pegando dados de um formulário, essa é a maneira.
    texto = request.form.get('texto', '')
    idade = request.form.get('idade', '')
    return render_template("index.html", saida=texto, saida2 = idade)
if __name__ == "__main__":
    app.run(debug=True)