import os
import bottle

@bottle.route('/')
def home_page():
	return bottle.template('index')

@bottle.post('/upload')
def do_upload():
	category = bottle.request.forms.get('category')
	upload = bottle.request.files.get('upload')
	name = bottle.request.forms.get('name')
	name, ext = os.path.splitext(upload.filename)
	directory = os.getcwd()

	if ext not in ('.png', '.jpg', '.jpeg'):
	  	message = "File extension not allowed."
	  	return bottle.template('img_resultado', {'message': message})

	save_path = "{directory}/img/{category}".format(directory=directory, category=category)

	if not os.path.exists(save_path):
	    os.makedirs(save_path)

	file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
	namefile = upload.filename
	archivo = "/" + category + "/" + upload.filename
	upload.save(file_path)
	message = "File successfully saved to '{0}'.".format(save_path)
	return bottle.template('img_resultado', {'name': name, 'namefile': namefile, 'img': archivo})

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='img')

bottle.debug(True)
bottle.run(host='localhost', port=8080)