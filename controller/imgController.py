# encoding: UTF-8
# Meus arquivos
from model.profile import Profile
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
#

@orm.db_session
def getImg(profile_id):
	perfil = orm.select(perfil for perfil in Profile if perfil.id == profile_id)[:]
	return str(perfil[0].picture)