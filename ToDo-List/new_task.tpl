<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    %#template for the form for a new task
    <p>Add a new task to the ToDo list:</p>
    <form action="/new" method="GET">
        <input type="text" size="100" maxlength="100" name="task">
        <input type="submit" name="save" value="save">
    </form>
</body>
</html>