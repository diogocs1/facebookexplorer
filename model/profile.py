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
	first_name = orm.Optional(str)
	last_name = orm.Optional(str)
	password = orm.Optional(str)
	verified = orm.Optional(bool)
	name = orm.Optional(str, unique=True)
	locale = orm.Optional(str)
	gender = orm.Optional(str)
	email = orm.Required(str)
	link = orm.Optional(str)
	timezone = orm.Optional(int)
	updated_time = orm.Optional(str)
	picture = orm.Optional(orm.buffer)
	picture_url = orm.Optional(str)
	# chaves estrangeiras Reversas
	from_posts = orm.Set("Post", reverse="from_")
	

class Friend(db.Entity):
	'''
	Entidade Relação Friend
	Representa a autorelação entre os perfis de usuário
	'''
	user_id = orm.Required(str)
	friend_name = orm.PrimaryKey(str)
	friend_picture = orm.Required(str)
