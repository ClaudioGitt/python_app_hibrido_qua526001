from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    # return chama as rotas.
    return render_template("Index.html")
if __name__ == "__main__":
    # O código acima, if name é para indicar que aqui é o arquivo principal.
    app.run(debug=True)