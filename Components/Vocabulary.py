import os
import json
import requests


class API:
    def __init__(self, url="https://od-api.oxforddictionaries.com/api/v2/entries/", language="es/"):
        self._url = url + language

    def getToken(self):
        with open("token.json", "r") as file:
            token = json.load(file)
        data = {
            "app_id": token[0]["app_id"],
            "app_key": token[0]["app_key"]
        }
        return data

    def definition(self, word):
        app_id = self.getToken()["app_id"]
        app_key = self.getToken()["app_key"]
        url = self._url + word
        response = requests.get(
            url, headers={'app_id': app_id, 'app_key': app_key})

        if response.status_code == 200:
            json_response = response.json()
            definition = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
            return definition

        else:
            print("Error: ", response.status_code, response.reason)
            exit()


class Vocabulary:
    def __init__(self):
        self._word_counter = 0
        self.api = API()

    def word_exists(self, word):
        with open("data.json", "r") as file:
            data = json.loads(file.read())
        for i in data:
            if i["word"] == word:
                return True
        return False

    def add_word(self, word):
        word = word.lower()
        if os.path.exists("data.json"):
            if not self.word_exists(word):
                with open("data.json", "r") as file:
                    js = json.loads(file.read())
                data = {
                    "word": word,
                    "definition": self.api.definition(word)
                }
                js.append(data)
                with open("data.json", "w") as file:
                    file.write(json.dumps(js, indent=4))
                print(
                    "\nWord added: {} - {}\n".format(word, self.api.definition(word))
                )
            else:
                print("Word already exists")
        else:
            with open("data.json", "w") as file:
                data = []
                file.write(json.dumps(data, indent=4))

    def delete_word(self, word):
        pass

    def show_all(self, letter=None):
        with open("data.json", "r") as file:
            data = json.loads(file.read())
        for i in data:
            print("{} - {}".format(i["word"], i["definition"]))
            print("-" * 20)

    def search_word(self, word):
        word = word.lower()
        if self.word_exists(word):
            with open("data.json", "r") as file:
                data = json.loads(file.read())
            for i in data:
                if i["word"] == word:
                    return i["definition"]
        else:
            return "Word not found"


class Menu(Vocabulary):
    def show(self):
        print("""
        1. Add word
        2. Delete word
        3. Show all words
        4. Search word
        5. Exit
        """)

    def get_choice(self):
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            self.show()
            choice = self.get_choice()
            if choice == "1":
                word = input("Enter word: ")
                self.add_word(word)
            elif choice == "2":
                word = input("Enter word: ")
                self.delete_word(word)
            elif choice == "3":
                self.show_all()
            elif choice == "4":
                word = input("Enter word: ")
                print(self.search_word(word))
            elif choice == "5":
                break
            else:
                print("Invalid choice")
