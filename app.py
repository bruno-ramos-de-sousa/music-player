from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

#funcao para fazer o get da primeira pagina do site
@app.route("/")
def index():
	return render_template("index.html")

#funcao para fazer o get da pagina do player
@app.route("/player")
def player():
	return render_template("player.html")


if __name__ == "__main__":
	app.run(debug=True)