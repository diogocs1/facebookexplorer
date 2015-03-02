# encoding: UTF-8
# Meus arquivos
from utils import Utils
from controller import homeController, imgController, grafoController, feedController
# Frameworks
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
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
	url = facebook.auth_url("573216906148994", "http://localhost:5000/token", perms=["user_friends", "email", "read_stream"])
	return render_template("login.html", url=url)

@app.route("/token")
def token():
	'''
	Usado para converter o 'code' retornado pela "auth_url" em 'access_token'
	'''
	code = request.args.get("code", '')
	if not Utils.token:
		Utils.token = facebook.get_access_token_from_code(code, "http://localhost:5000/token", "573216906148994", "1e7c79732df000c0bb045327e1da5379")
		Utils.api = facebook.GraphAPI(Utils.token["access_token"])
	return redirect(url_for("homeLoad"))

@app.route("/home")
def home():
	'''
	GET  /home
	Carrega a página inicial
	'''
	perfil_publico =  Utils.api.get_object("me")
	perfil_publico["picture"] = Utils.api.get_object("me/picture")["data"]
	perfil_publico["is_user"] = True

	# Salva os amigos
	amigos = Utils.api.get_connections("me", "taggable_friends")
	for amigo in amigos["data"]:
		amigo["is_user"] = False
		amigo["picture_url"] = amigo["picture"]["data"]["url"]
		del amigo["picture"]
		# Grava no banco
		homeController.salvaPerfil(amigo)

	# Grava no banco
	homeController.salvaPerfil(perfil_publico)
	# Apaga o binário da imagem do contexto de renderização e adiciona o link
	perfil_publico["picture"] = "http://localhost:5000/picture/%s.jpg" % (perfil_publico["id"])

	return render_template("home.html", perfil_publico=perfil_publico, logout=url_for("index"), amigos=amigos)

@app.route("/feed")
def feed():
	'''
	GET  /feed
	Armazena e retorna suas atualizações recentes
	'''
	feed = Utils.api.get_object("me/feed")

	Utils.post_cursor = feed["paging"]
	posts = feed["data"]
	
	feedController.salvaPosts(posts)

	usuario = feedController.obtemPerfilUsuario()
	return render_template("feed.html", perfil_publico=usuario)


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
	print 
	print pid
	print
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
	grafo = grafoController.getGrafo()
	return jsonify(**grafo)