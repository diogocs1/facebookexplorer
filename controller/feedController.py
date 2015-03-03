# encoding: UTF-8
# Meus arquivos
from model.profile import Profile
from model.feed import Post, Actions
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
#

@orm.db_session
def obtemPerfilUsuario():
	usuario = orm.select(
			perfil for perfil in Profile if perfil.is_user == True
		)[:]
	usuario = usuario[0]

	usuario_json = {
		"id" : usuario.id,
		"picture" : "http://localhost:5000/picture/%s.jpg" %(usuario.id),
		"first_name" : usuario.first_name
	}
	return usuario_json

@orm.db_session
def salvaPosts(posts):
	for post in posts:
		# Salvando as actions
		actions_list = []
		# Gerando a lista de atributos dinamicamente
		for action in post["actions"]:
			actions = "actions = Actions("
			for chave in action:
				actions += "%s = action['%s'], " % (chave, chave)
			actions += ")"
			exec actions
			actions_list.append(actions)
		# Criando a relação "from_"
		from_ = obterPerfilObj(post["from"]["id"])
		# Criando a relação "message_tags"
		if post.has_key("message_tags"):
			print post["message_tags"]
		else:
			print post.keys()


@orm.db_session
def obterPerfilObj(pid):
	perfil = orm.select(perfil for perfil in Profile if perfil.id == pid)[:][0]
	return perfil