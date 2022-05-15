import json

with open("./Data/data.json", "r") as file:
    data = json.loads(file.read())
    export = ""
    for i in data:
        export += i["word"] + " - " + i["definition"]  + "\n\n"

with open("./Data/data.txt", "w") as file:
    file.write(export)