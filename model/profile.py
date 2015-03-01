# encoding: UTF-8
# Meus arquivos
from utils import Utils
# Frameworks
import pony.orm as orm
# Bibliotecas padrão


db = Utils.banco

class Profile(db.Entity):
	'''
	Entidade Profile
	Exemplo: /me
	'''
	id = orm.PrimaryKey(str)
	is_user = orm.Required(bool)
	first_name = orm.Optional(str)
	last_name = orm.Optional(str)
	verified = orm.Optional(bool)
	name = orm.Optional(str, unique=True)
	locale = orm.Optional(str)
	gender = orm.Optional(str)
	email = orm.Optional(str)
	link = orm.Optional(str)
	timezone = orm.Optional(int)
	updated_time = orm.Optional(str)
	picture = orm.Optional(orm.buffer)
	picture_url = orm.Optional(str)


db.generate_mapping(create_tables=True)