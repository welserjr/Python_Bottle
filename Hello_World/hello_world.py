import bottle

@bottle.route('/')
def home_page():
	mythings = ['Developer Python', 'Front-end', 'Developer iOS', 'Back-end', 'MongoDB']
	return bottle.template('hello_world', username="Welser", things=mythings)
	#return bottle.template('hello_world', {'username': "Welser",
	#                                       'things': mythings})

bottle.debug(True)
bottle.run(host='localhost', port=8080)