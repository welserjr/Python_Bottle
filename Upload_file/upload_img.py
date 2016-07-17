import os
import bottle

@bottle.route('/')
def home_page():
	return bottle.template('index')

@bottle.post('/upload')
def do_upload():
	upload = bottle.request.files.get('upload')
	name = bottle.request.forms.get('name')
	directory = os.getcwd()

	save_path = "{directory}/files".format(directory=directory)

	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
	upload.save(file_path)
	message = "File successfully saved to '{0}'.".format(save_path)
	return bottle.template('file_resultado', {'name': name})

bottle.debug(True)
bottle.run(host='localhost', port=8080)