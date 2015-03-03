# encoding: UTF-8
# Meus arquivos
from model.profile import Profile
from model.feed import Post, Actions, Tag, Privacy, Comment
# Frameworks
import pony.orm as orm
# Bibliotecas padrão
#

@orm.db_session
def obtemPerfilUsuario(pid):
	usuario = orm.select(
			perfil for perfil in Profile if perfil.id == pid
		)[:]
	usuario = usuario[0]

	usuario_json = {
		"id" : usuario.id,
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
		tags = []
		if post.has_key("message_tags"):
			for chave in post["message_tags"]:
				for valor in post["message_tags"][chave]:				
					tag = Tag(
							uid = valor["id"],
							name = valor["name"]
						)
					tags.append(tag)
		# Criando a relação Privacy
		privacy =  Privacy(
					allow = post["privacy"]["allow"],
					deny = post["privacy"]["deny"],
					friends = post["privacy"]["friends"],
					description = post["privacy"]["description"],
					value = post["privacy"]["value"]
			)
		# Pegando os comentários
		comments = []
		if post.has_key("comments"):
			for comm in post["comments"]["data"]:
				comment = Comment(
							id = comm["id"],
							from_name = comm["from"]["name"],
							like_count = comm["like_count"],
							can_remove = comm["can_remove"],
							created_time = comm["created_time"],
							message = comm["message"],
							user_likes = comm["user_likes"]
					)
				comments.append(comment)
		# definindo o atributos opcionais
		application = ""
		caption = ""
		description = ""
		icon = ""
		is_hidden = False
		link = ""
		message = ""
		name = ""
		object_id = ""
		picture = ""
		place = ""
		shares = 0
		source = ""
		status_type = ""
		story = ""
		type_ = ""
		updated_time = ""
		if post.has_key("application"):
			application = str(post["application"])
		if post.has_key("caption"):
			caption = post["caption"]
		if post.has_key("description"):
			description = post["description"]
		if post.has_key("icon"):
			icon = post["icon"]
		if post.has_key("is_hidden"):
			is_hidden = post["is_hidden"]
		if post.has_key("link"):
			link = post["link"]
		if post.has_key("message"):
			message = post["message"]
		if post.has_key("name"):
			name = post["name"]
		if post.has_key("object_id"):
			object_id = post["object_id"]
		if post.has_key("picture"):
			picture = post["picture"]
		if post.has_key("place"):
			place = post["place"]
		if post.has_key("shares"):
			shares = post["shares"]
		if post.has_key("source"):
			source = post["source"]
		if post.has_key("status_type"):
			status_type = post["status_type"]
		if post.has_key("story"):
			story = post["story"]
		if post.has_key("type"):
			type_ = post["type"]
		if post.has_key("updated_time"):
			updated_time = post["updated_time"]
		# Criando o objeto Post
		Post(
			id = post["id"],
			actions = actions_list,
			application = application,
			caption = caption,
			created_time = post["created_time"],
			description = description,
			from_ = from_,
			icon = icon,
			is_hidden = is_hidden,
			link = link,
			message = message,
			message_tags = tags,
			name = name,
			object_id = object_id,
			picture = picture,
			place = place,
			privacy = privacy,
			comments = comments,
			shares = shares,
			source = source,
			status_type = status_type,
			story = story,
			type_ = type_,
			updated_time = updated_time
		)
		try:
			orm.commit()
		except:
			print "Post já cadastrado!"

@orm.db_session
def obterPosts(pid):
	posts = orm.select(post for post in Post if post.from_.id == pid)[:]
	return posts

@orm.db_session
def obterPerfilObj(pid):
	perfil = orm.select(perfil for perfil in Profile if perfil.id == pid)[:][0]
	return perfil