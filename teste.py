from appkit.api.v0_2_8 import App

app = App(__name__)

@app.route("/")
def home():
	return '<a href="#" target="_blank">Clique</a>'

app.run()
