<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Lenguaje Favorito</title>
</head>
<body>
	<p>Welcome {{username}}</p>

	<ul>
		%for language in languages:
			<li>{{language}}</li>
		%end
	</ul>
	<form action="/favorite_language" method="POST">
		¿Cuál es tu lenguaje favorito?
		<input type="text" name="language" size="40" value=""><br>
		<input type="submit" value="Submit">
	</form>
</body>
</html>