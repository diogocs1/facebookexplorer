# encoding: UTF-8
# Meus arquivos
from model.profile import Profile, Friend
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
from math import sin, cos
from random import randint

@orm.db_session
def getGrafo(uid):
	# recupera os amigos
	amigos = orm.select(
			amigo for amigo in Friend if amigo.user_id == uid
		)[:]
	usuario = orm.select(
			perfil for perfil in Profile if perfil.id == uid
		)[:]
	# cria a estrutura do grafo JSON
	grafo = {"g":
				 {"nodes": [],
				  "edges": []
				 }
			}
	# Adiciona o nó central
	grafo["g"]["nodes"].append({
			"id" : "n0",
			"label" : usuario[0].name,
			"x" : 0,
			"y" : 0,
			"size" : 5,
			"color" : '#ec5148'
	})
	# Carrega os amigos na estrutura
	cont = 1
	rotacao = 1
	div = 1440 / len(amigos)
	for amigo in amigos:
		sub = randint(0,100) / 100.0
		# adicionando o nó
		grafo["g"]["nodes"].append({
				"id" : "n" + str(cont),
				"label" : amigo.friend_name,
				"x" : sin(rotacao) - sub,
				"y" : cos(rotacao) - sub,
				"size" : 2,
				"color" : '#ec5148'
			})
		# adicionando o vértice
		grafo["g"]["edges"].append({
				"id" : "e" + str(cont),
				"source" : "n0",
				"target" : "n" + str(cont),
			})
		cont += 1
		rotacao += div
	return grafo["g"]