from flask import Flask, url_for, redirect, jsonify, render_template
import lib.twitterapi as tw


app = Flask(__name__)
app.debug = True # Eliminar para producción


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/q/<query>/json")
def buscar_json(query):
    tweets = tw.search(query)
    return jsonify(tweets)

@app.route("/q/<query>")
def buscar_html(query):
    tweets = tw.search(query)
    return render_template("resultados.html", tweets=tweets)


if __name__ == '__main__':
        app.run()
