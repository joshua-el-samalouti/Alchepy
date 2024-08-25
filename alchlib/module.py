import json
import pandas as pd


# TODO: refactor dataframes to work with column labels instead of indices
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
    def unlock_element(self, element: str):
        self.elements.loc[self.elements[0] == element, 2] = 1
        if self.debug_mode is True:
            print(self.elements.loc[self.elements[0] == element])
            print("DEBUG: element ", element, "was unlocked")

    # marks the given element as undiscovered
    def lock_element(self, element: str):
        self.elements.loc[self.elements[0] == element, 2] = 0
        if self.debug_mode is True:
            print(self.elements.loc[self.elements[0] == element])

    # marks the given recipe as discovered
    def unlock_recipe(self, recipe_id: int):
        self.recipes[recipe_id][3] = 1
        if self.debug_mode is True:
            print(self.recipes[recipe_id])

    # marks the given recipe as undiscovered
    def lock_recipe(self, recipe_id: int):
        self.recipes[recipe_id][3] = 0
        if self.debug_mode is True:
            print(self.recipes[recipe_id])

    # returns the recipe id if the given elements match, returns -1 if they don't match. Considers symmetry option
    def find_recipe(self, element_1: str, element_2: str):
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

    def get_recipe(self, recipe_id):
        if self.debug_mode is True:
            print("Recipe #",recipe_id,": ",self.recipes[recipe_id])
        return self.recipes[recipe_id]

    # checks if the given element is valid and discovered or not
    def is_unlocked_element(self, element: str):
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

    # checks if the recipe of a given ID is discovered or not
    def is_discovered_recipe(self, recipe_id: int):
        if self.get_recipe(recipe_id)[3] == 1:
            if self.debug_mode is True:
                print(recipe_id, " is discovered")
            return True
        else:
            if self.debug_mode is True:
                print(recipe_id, " is not discovered")
            return False

    def get_unlocked_groups(self):
        group_list = []
        for group in self.elements.loc[self.elements[2] == 1][1].unique():
            group_list.append(group)
        return group_list

    # TODO: ADD DEBUG MESSAGES
    # TODO: REFACTOR OUTPUT TO BE MORE INTUITIVE
    # checks if given elements match and unlocks recipe and result if they do
    # returns [-1,-1,[]] if elements are invalid or locked
    # returns [0,-1,[]] if elements don't match
    # returns [1, recipe_id,[]] if elements match, but the recipe was discovered already
    # returns [2, recipe_id, []] if elements match, the results were discovered already,
    # but the recipe is new
    # returns [3, recipe_id,[new_elements]] if elements match and there is one or more
    # new elements unlocked
    # the format is [status, recipe id, [unlocked elements]]
    def match_elements(self, element_1: str, element_2: str):
        unlocked_1 = self.is_unlocked_element(element_1)
        unlocked_2 = self.is_unlocked_element(element_2)
        if unlocked_1 and unlocked_2:
            recipe_id = self.find_recipe(element_1, element_2)
            if recipe_id >= 0:
                # elements match
                recipe = self.get_recipe(recipe_id)
                if recipe[3] == 1:
                    # the recipe was discovered already
                    return [1, recipe_id, []]
                else:
                    # the recipe was not discovered yet
                    self.unlock_recipe(recipe_id)
                    newly_unlocked = []

                    # TODO: make this part work for recipes with multiple results
                    if not self.is_unlocked_element(recipe[2]):
                        newly_unlocked.append(recipe[2])
                        self.unlock_element(recipe[2])
                        
                    if len(newly_unlocked) == 0:
                        # there are no newly unlocked elements
                        return [2, recipe_id, []]
                    else:
                        # there are newly unlocked elements
                        return [3, recipe_id, newly_unlocked]
            else:
                # elements don't match
                return [0, -1, []]
        else:
            # one or more elements are invalid or locked
            # no information about which element is invalid is returned
            # for information about this other methods have to be used additionally
            return [-1, -1, []]
