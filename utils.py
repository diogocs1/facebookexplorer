# encoding: UTF-8

import pony.orm as orm


class Utils(object):
	# GraphAPI Object
	api = None
	# Token String
	token = ""
	# PonyORM Database connection
	banco = orm.Database("sqlite", "facebook.db", create_db=True)
	post_cursor = None
	pid = ""