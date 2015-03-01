# encoding: UTF-8
# Meus arquivos
from flaskapp import app
from utils import Utils
# Frameworks
import webview
import facebook
import pony.orm as orm
# Bibliotecas padrão
import thread
import time


def startApp():
	'''
	Inicia a visualização web embutida
	'''
	time.sleep(1)
	webview.create_window("Facebook Explorer", "http://localhost:5000", width=1000, height=600)

def startServer():
	'''
	Inicia o servidor web e chama createdb() para criar o banco de dados
	'''
	# remover debug em versão final
	app.run(debug=True)


if __name__ == "__main__":
	thread.start_new_thread(startApp, ())
	startServer()