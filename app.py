from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Awsome_secret_key"

@app.route("/hello")
def index():
    flash("Qual seu nome?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Olá, " + str(request.form['name_input']) + "! " + "Bom te conhecer :)")
    return render_template('index.html')    