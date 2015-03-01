# encoding: UTF-8
# Meus arquivos
from model.profile import Profile
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
		"picture" : "http://localhost:5000/%s.jpg" %(usuario.id),
		"first_name" : usuario.first_name
	}
	return usuario_json