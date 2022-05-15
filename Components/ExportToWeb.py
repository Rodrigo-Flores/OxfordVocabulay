from string import Template
from Vocabulary import Vocabulary

cuerpo_tabla = ""
html = Template(
    """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <title>Pokemon</title>
</head>
<body>
    <table class="table">
        <tr>
            <th>Palabra</th>
            <th>Definición</th>
        </tr>
        $cuerpo_tabla
    </table>
</body>
</html>
""")

data = Vocabulary()
data = data.get_all()

for i in data:
    word = i["word"]
    definition = i["definition"]

    cuerpo_tabla += Template(
        """
    <tr>
        <td>${word}</td>
        <td>${definition}</td>
    </tr>
    """).substitute(word=word, definition=definition)

with open("./Data/index.html", "w") as file:
    file.write(html.substitute(cuerpo_tabla=cuerpo_tabla))