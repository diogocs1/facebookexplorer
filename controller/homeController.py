# encoding: UTF-8
# Meus arquivos
from model.profile import Profile, Friend
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
#

@orm.db_session
def salvaPerfil(json):
	'''
	Salva o perfil do usuário usando apenas os campos obtidos no JSON
	'''
	perfil = "perfil = Profile("

	for chave in json:
		perfil += "%s = json['%s']," % (chave, chave)

	perfil += ")"
	exec perfil
	try:
		orm.commit()
	except:
		print "Perfil já cadastrado!"

@orm.db_session
def salvaAmigo(json, user_id):
	'''
	Salva o amigo na tabela Friend
	'''
	for amigo in json:
		Friend(
				user_id=user_id,
				friend_name = amigo["name"],
				friend_picture = amigo["picture"]["data"]["url"]
			)
		try:
			orm.commit()
		except:
			print "Perfil já cadastrado!"