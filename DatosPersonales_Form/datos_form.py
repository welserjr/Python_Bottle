import bottle

@bottle.error(404)
def not_found(error):
	return bottle.template('error')

@bottle.route('/')
def home_page():
	return bottle.template('index')


@bottle.post('/datos_personales')
def datos_personales():
	nombre = bottle.request.forms.get("nombre")
	apellidos = bottle.request.forms.get("apellidos")
	edad = bottle.request.forms.get("edad");
	email = bottle.request.forms.get("email")

	return bottle.template('datos_resultado', {'nombre': nombre,
		                                           'apellidos': apellidos,
		                                           'edad': edad,
		                                           'email': email})

bottle.debug(False)
bottle.run(host='0.0.0.0', port=8080)