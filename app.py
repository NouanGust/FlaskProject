from flask import Flask, render_template, request, flash
import emoji

app = Flask(__name__)
app.secret_key = "Awsome_secret_key"

@app.route("/hello")
def index():
    flash("...")
    flash('')
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    if str(request.form['name_input']) != '':
        flash("Saudações " + str(request.form['name_input']) + str(emoji.emojize(":vulcan_salute:")))
        flash("Bom te conhecer!")
    else:
        flash("Tente digitar seu nome ou um nome qualquer. Não se preocupe, esse site não guarda seus dados.")
    return render_template('index.html')    