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
		# Verifica se o atributo existe no banco de dados local,cas
		if chave in ["id", "first_name", "last_name", "password", "verified", "name", "locale", "gender", "email", "link", "timezone", "updated_time","picture", "picture_url"]:
			perfil += "%s = json['%s']," % (chave, chave)
	perfil += ")"
	exec perfil
	try:
		orm.commit()
	except:
		print "Perfil já cadastrado!"

@orm.db_session
def obterPerfil(pid):
	perfil = orm.select(perfil for perfil in Profile if perfil.id == pid)[:][0]
	return perfil

@orm.db_session
def obterPerfilPorEmail(email_arg):
	perfil = orm.select(perfil for perfil in Profile if perfil.email == email_arg)[:]
	return perfil

@orm.db_session
def salvaAmigo(json, user_id):
	'''
	Salva o amigo na tabela Friend
	'''
	for amigo in json:
		try:
			Friend(
					user_id=user_id,
					friend_name = amigo["name"],
					friend_picture = amigo["picture"]["data"]["url"]
				)
		
			orm.commit()
		except:
			print "Perfil já cadastrado!"

@orm.db_session
def setSenha(perfil, senha):
	perf = orm.select(perf for perf in Profile if perf.id == perfil.id)[:][0]
	perf.password = senha

@orm.db_session
def obterAmigos(pid):
	amigos = orm.select(amigo for amigo in Friend if amigo.user_id == pid)[:]
	return amigos