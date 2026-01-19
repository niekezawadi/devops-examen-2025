from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    joke = None

    if request.method == "POST":
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        data = response.json()
        joke = data["value"]

    return render_template("index.html", joke=joke)

app.run(host="0.0.0.0", port=5000)
