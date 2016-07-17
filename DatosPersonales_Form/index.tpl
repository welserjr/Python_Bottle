<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Datos Personales</title>
</head>
<body>
	<h1>Datos Personales</h1>
	<form action="/datos_personales" method="POST">
		<input type="text" name="nombre" size="18" placeholder="Nombre">
		<input type="text" name="apellidos" size="20" placeholder="Apellidos"><br>
		<input type="text" name="edad" size="6" placeholder="Edad">
		<input type="text" name="email" size="32" placeholder="Correo Electrónico"><br>
		<input type="submit" value="Guardar">
	</form>
</body>
</html>