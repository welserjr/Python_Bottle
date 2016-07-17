import bottle

__author__ = "Welser Muñoz"

@bottle.error(404)
def not_found(error):
	return bottle.template('views/error')

@bottle.route('/')
def home_page():
	return bottle.template('views/index')

@bottle.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='static/css')

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='static/img')

bottle.debug(True)
bottle.run(host='localhost', port=8080)