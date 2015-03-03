# encoding: UTF-8
# Meus arquivos
from utils import Utils
from controller import homeController, imgController, grafoController, feedController
# Frameworks
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, Response
from functools import wraps
import facebook
# Bibliotecas padrão
#

app = Flask(__name__)

# URL's


@app.route("/refresh_facebook_data", methods=["GET", "POST"])
def refresh():
	if not Utils.api:
		url = facebook.auth_url("573216906148994", "http://localhost:5000/token", perms=["user_friends", "email", "read_stream", "read_mailbox"])
		return redirect(url)
	# Recuperando os objetos
	perfil_publico =  Utils.api.get_object("me")
	perfil_publico["picture"] = Utils.api.get_object("me/picture")["data"]
	amigos = Utils.api.get_connections("me", "taggable_friends")
	feed = Utils.api.get_object("me/feed")

	conversations = Utils.api.get_object("me?fields=conversations")
	
	posts = feed["data"]
	print conversations["conversations"]["data"][0]
		
	# Grava no banco
	homeController.salvaAmigo(amigos["data"], perfil_publico["id"])
	homeController.salvaPerfil(perfil_publico)
	feedController.salvaPosts(posts)
	if request.method == "GET":
		return redirect(url_for("login"))
	else:
		return redirect(url_for("home"))

@app.route("/token")
def token():
	'''
	Usado para converter o 'code' retornado pela "auth_url" em 'access_token'
	'''
	code = request.args.get("code", '')
	if not Utils.token:
		Utils.token = facebook.get_access_token_from_code(code, "http://localhost:5000/token", "573216906148994", "1e7c79732df000c0bb045327e1da5379")
		Utils.api = facebook.GraphAPI(Utils.token["access_token"])
	return redirect(url_for("refresh"))

@app.route("/login", methods=["GET", "POST"])
def login():
	# Primeira vez de login, defina uma senha para acesso local
	set_senha = False
	if Utils.api:
		set_senha = True
	if request.method == "GET":
		return render_template("login.html", set_senha=set_senha)
	elif request.method == "POST":
		email = request.form["email"]
		senha = request.form["senha"]
		perfil = homeController.obterPerfilPorEmail(email)
		if perfil and set_senha:
			# Definindo a nova senha para acesso local e redirecionando para a tela inicial
			homeController.setSenha(perfil[0], senha)
			Utils.pid = perfil[0].id
			return redirect(url_for("home"))
		elif perfil:
			# Verifica usuário já cadastrado
			if perfil[0].password == senha:
				Utils.pid = perfil[0].id
				print Utils.pid
				return redirect(url_for("home"))
			else:
				return redirect(url_for("login"))
		else:
			# Realiza a coleta de dados do facebook
			return redirect(url_for("refresh"))

@app.route("/home")
def home():
	'''
	GET  /home
	Carrega a página inicial
	'''
	perfil_publico = homeController.obterPerfil(Utils.pid)
	amigos = homeController.obterAmigos(Utils.pid)

	return render_template("home.html", perfil_publico=perfil_publico, logout=url_for("login"), amigos=amigos)

@app.route("/feed")
def feed():
	'''
	GET  /feed
	Armazena e retorna suas atualizações recentes
	'''
	usuario = feedController.obtemPerfilUsuario(Utils.pid)
	posts = feedController.obterPosts(Utils.pid)
	print posts
	return render_template("feed.html", perfil_publico=usuario, posts=posts, len_posts=len(posts))


@app.route("/home/load")
def homeLoad():
	'''
	GET  /home/load
	Mostra tela de carregando antes de iniciar o sistema
	'''
	return render_template("carregando.html")

# retorna as fotos salvas no banco
@app.route("/picture/<pid>.jpg")
def getImage(pid):
	'''
	GET  /picture/*.jpg
	Mapeia imagens do banco como links
	'''
	image = imgController.getImg(pid)
	response = make_response(image)
	response.headers['Content-Type'] = 'image/jpeg'
	response.headers['Content-Disposition'] = 'attachment; filename=img.jpg'
	return response

@app.route("/grafo.json")
def grafoJson():
	'''
	GET  /grafo.json
	Retorna o objeto JSON usado no grafo de conexões
	'''
	grafo = grafoController.getGrafo(Utils.pid)
	return jsonify(**grafo)


