import json
import pandas as pd


class Module:

    # upon initialization reads the given json file and assigns the data to the object attributes
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

    # prints out a lot of attributes of the object and their data types
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

    # debug mode makes some functions print additional information into the console
    def toggle_debug(self):
        if self.debug_mode is False:
            self.debug_mode = True
            print("Debug mode enabled")
        else:
            self.debug_mode = False
            print("Debug mode disabled")

    # marks the given element as discovered
    def unlock_element(self, element):
        self.elements.loc[self.elements[0] == element, 2] = 1
        if self.debug_mode is True:
            print(self.elements.loc[self.elements[0] == element])

    # marks the given element as undiscovered
    def lock_element(self, element):
        self.elements.loc[self.elements[0] == element, 2] = 0
        if self.debug_mode is True:
            print(self.elements.loc[self.elements[0] == element])

    # marks the given recipe as discovered
    def unlock_recipe(self, recipe_id):
        self.recipes[recipe_id][3] = 1
        if self.debug_mode is True:
            print(self.recipes[recipe_id])

    # marks the given recipe as undiscovered
    def lock_recipe(self, recipe_id):
        self.recipes[recipe_id][3] = 0
        if self.debug_mode is True:
            print(self.recipes[recipe_id])

    # returns the recipe id if the given elements match, otherwise returns -1
    def find_recipe_id(self, element_1, element_2):
        pass

    # checks if the given element is discovered or not
    def is_unlocked_element(self, element):
        if element in self.elements.loc[self.elements[2] == 1, 0]:
            if self.debug_mode is True:
                print(element, " is valid: ", self.elements.loc[self.elements[0] == element])
            return True
        else:
            if self.debug_mode is True:
                print(element, " is not valid")
            return False
