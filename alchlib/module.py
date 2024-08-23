import json
import pandas as pd


class Module:
    def __init__(self, path: str):
        f = open(path)
        data = json.load(f)
        f.close()
        self.title = data['title']
        self.description = data['description']
        self.introduction = data['introduction']
        self.elements = pd.DataFrame(data['elements'])
        self.recipes = pd.DataFrame(data['recipes'])
        self.options = data['options']
        self.info = data['info']
        self.version = data['version']
        self.author = data['author']
        self.debug_mode = False

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}"

    def debug_info(self):
        print(type(self.title))
        print(self.title)
        print(type(self.description))
        print(self.description)
        print(type(self.introduction))
        print(self.introduction)
        print(type(self.elements))
        print(self.elements)
        print(type(self.recipes))
        print(self.recipes)
        print(type(self.options))
        print(self.options)
        print(type(self.info))
        print(self.info)
        print(type(self.version))
        print(self.version)
        print(type(self.author))
        print(self.author)

    def toggle_debug(self):
        if self.debug_mode is False:
            self.debug_mode = True
            print("Debug mode enabled")
        else:
            self.debug_mode = False
            print("Debug mode disabled")

    def unlock(self, element):
        self.elements.loc[self.elements[0] == element, 2] = 1
        if self.debug_mode is True:
            print(self.elements.loc[self.elements[0] == element])


