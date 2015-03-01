# encoding: UTF-8
# Meus arquivos
from model.profile import Profile
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
