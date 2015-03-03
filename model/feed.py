# encoding: UTF-8
# Meus arquivos
from utils import Utils
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
from datetime import datetime

db = Utils.banco

class Post(db.Entity):
	'''
	Entidade Post
	Representa as atualizações do usuário
	'''
	id = orm.PrimaryKey(str)
	actions = orm.Set("Actions")
	application = orm.Required(str)
	caption = orm.Optional(str)
	created_time = orm.Required(datetime)
	description = orm.Optional(str)
	from_ = orm.Required("Profile")
	icon = orm.Optional(str)
	is_hidden = orm.Optional(bool)
	link = orm.Optional(str)
	message = orm.Optional(str)
	message_tags = orm.Set("Tag")
	name = orm.Optional(str)
	object_id = orm.Optional(str)
	picture = orm.Optional(str)
	place = orm.Optional(str)
	privacy = orm.Required("Privacy")
	properties = orm.Optional("Properties")
	shares = orm.Optional(int)
	source = orm.Optional(str)
	status_type = orm.Optional(str)
	story = orm.Optional(str)
	to = orm.Set("Profile")
	type_ = orm.Optional(str)
	updated_time = orm.Optional(datetime)
	with_tags = orm.Set("Profile")


class Actions(db.Entity):
	'''
	Entidade Actions
	Representa o objeto "Actions" que compõe a entidade Post
	'''
	name = orm.Required(str)
	link = orm.Required(str)
	post = orm.Optional("Post")

class Tag(db.Entity):
	'''
	Entidade Tag
	Representa o objeto "message_tags" que compõe a entidade Post
	'''
	uid = orm.Required(str)
	name = orm.Required(str)
	post = orm.Required("Post")

class Privacy(db.Entity):
	'''
	Entidade Privacy
	Representa o objeto "privacy" que compõe a entidade Post
	'''
	description = orm.Required(str)
	value = orm.Required(str)
	friends = orm.Required(str)
	allow = orm.Required(str)
	deny = orm.Required(str)
	post = orm.Optional("Post")

class Properties(db.Entity):
	'''
	Entidade Properties
	Representa o objeto "properties" que compõe a entidade Post
	'''
	name = orm.Required(str)
	text = orm.Optional(str)
	href = orm.Optional(str)
	post = orm.Optional("Post")
