import bottle

@bottle.route('/')
def home_page():
	mylanguages = ['Python', 'Objective-C', 'Ruby', 'PHP', 'JavaSCript']
	#return bottle.template('hello_world', username= "Welser",  'languages' = mylanguages)
	return bottle.template('hello_world', {'username': "Welser",
		                                   'languages': mylanguages})

@bottle.post('/favorite_language')
def favorite_language():
	language = bottle.request.forms.get("language")
	if(language == None or language == ""):
		language = "Lenguaje No Ingresado!!!"

	bottle.response.set_cookie("language", language)
	bottle.redirect("/show_language")

@bottle.route('/show_language')
def show_language():
	fruit = bottle.request.get_cookie("language")
	return bottle.template('language_selection.tpl', {'language': language})

bottle.debug(True)
bottle.run(host='localhost', port=8080)