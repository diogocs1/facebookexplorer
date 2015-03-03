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
	application = orm.Optional(str)
	caption = orm.Optional(str)
	created_time = orm.Required(str)
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
	comments = orm.Set("Comment")
	shares = orm.Optional(int)
	source = orm.Optional(str)
	status_type = orm.Optional(str)
	story = orm.Optional(str)
	type_ = orm.Optional(str)
	updated_time = orm.Optional(str)


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
	post = orm.Optional("Post")

class Privacy(db.Entity):
	'''
	Entidade Privacy
	Representa o objeto "privacy" que compõe a entidade Post
	'''
	description = orm.Optional(str)
	value = orm.Optional(str)
	friends = orm.Optional(str)
	allow = orm.Optional(str)
	deny = orm.Optional(str)
	post = orm.Optional("Post")

class Comment(db.Entity):
	'''
	Entidade Properties
	Representa o objeto "properties" que compõe a entidade Post
	'''
	id = orm.PrimaryKey(str)
	from_name = orm.Optional(str)
	like_count = orm.Optional(int)
	can_remove = orm.Optional(bool)
	created_time = orm.Optional(str)
	message = orm.Optional(str)
	user_likes = orm.Optional(bool)
	post = orm.Optional("Post")