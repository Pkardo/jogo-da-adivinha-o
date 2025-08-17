from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

numero_secreto = randint(0, 5)
tentativas = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global tentativas, numero_secreto
    mensagem = ""

    if request.method == "POST":
        tentativa = int(request.form.get("numero"))
        tentativas += 1
        
        if tentativa == numero_secreto:
            mensagem = f"🎉 Você acertou em {tentativas} tentativas! O número era {numero_secreto}."
            numero_secreto = randint(0, 5)
            tentativas = 0
        else:
            mensagem = "❌ Errou! Tente novamente."

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
