<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Upload File</title>
</head>
<body>
	<h1>Guardar Archivo</h1>
	<form action="/upload" method="post" enctype="multipart/form-data">
  		Nombre:        <input type="text" name="name" />
  		Select a file: <input type="file" name="upload" />
  		<input type="submit" value="Start upload" />
	</form>
</body>
</html>