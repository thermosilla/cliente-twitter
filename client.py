from flask import Flask, url_for, redirect, jsonify, render_template
import lib.twitterapi as tw

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return "Página de prueba"

@app.route("/q/<query>")
def buscar(query):
    tweets = tw.search(query)
    return jsonify(tweets)

if __name__ == '__main__':
        app.run()
