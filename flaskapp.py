# encoding: UTF-8
# Meus arquivos
from utils import Utils
# Frameworks
from flask import Flask, render_template, request, redirect, url_for
import facebook
# Bibliotecas padrão
#

app = Flask(__name__)

# URL's

@app.route("/")
def index():
	'''
	GET  /
	Carrega a página de verificação de autenticação
	'''
	url = facebook.auth_url("573216906148994", "http://localhost:5000/token")
	return render_template("login.html", url=url)

@app.route("/token")
def token():
	code = request.args.get("code", '')
	if not Utils.token:
		Utils.token = facebook.get_access_token_from_code(code, "http://localhost:5000/token", "573216906148994", "1e7c79732df000c0bb045327e1da5379")
	return redirect(url_for("home"))

@app.route("/home")
def home():
	'''
	GET  /home
	Carrega a página inicial
	'''
	api = facebook.GraphAPI(Utils.token["access_token"], version="2.0")
	print api.get_version()
	return render_template("login.html")