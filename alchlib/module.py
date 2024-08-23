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

    # returns the recipe id if the given elements match, returns -1 if they don't match. Considers symmetry option
    def find_recipe(self, element_1, element_2):
        subset = self.recipes.loc[self.recipes[0] == element_1].loc[self.recipes[1] == element_2]
        # remember to add symmetry
        if subset.empty and self.options['symmetry'] == 1:
            subset = self.recipes.loc[self.recipes[0] == element_2].loc[self.recipes[1] == element_1]
        if subset.empty:
            if self.debug_mode is True:
                print(element_1, " and ", element_2, " does not match")
            return -1
        else:
            recipe_id = int(subset.index[0])
            if self.debug_mode is True:
                print(element_1, " and ", element_2, " matches")
                print("subset: ", subset)
                print("index: ", recipe_id)
            return recipe_id
        pass

    # checks if the given element is discovered or not
    def is_unlocked_element(self, element):
        subset = self.elements.loc[self.elements[2] == 1].loc[self.elements[0] == element]
        if subset.empty:
            if self.debug_mode is True:
                print(subset)
                print(element, " is not valid")
            return False
        else:
            if self.debug_mode is True:
                print(subset)
                print(element, " is valid")
            return True
