import lib.twitterapi as tw
import urllib.parse as url

from flask import Flask, url_for, redirect, jsonify, render_template, request


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
def buscar_html(query=False):
    if not query:
        query = request.form['q']
    tweets = tw.search(query)
    return render_template("resultados.html", tweets=tweets)


@app.route("/search", methods=['POST'])
def buscar_post():
    query = request.form['q']
    return redirect(url_for('buscar_html', query=url.quote(query)))
    

if __name__ == '__main__':
        app.run()
