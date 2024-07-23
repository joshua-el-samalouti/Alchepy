import pandas as pd
import localization as loc


def placeholder_loader(lang):
    title = loc.placeholder_title[lang]
    description = loc.placeholder_description[lang]
    elements = pd.DataFrame([
        ['Fire', 'Energy', True],
        ['Water', 'Liquids', True],
        ['Earth', 'Earth', True],
        ['Air', 'Air', True],
        ['Steam', 'Air', False]
    ],
        columns=['name', 'group', 'unlocked'])
    recipes = pd.DataFrame([
        ['Fire', 'Water', ['Steam'], True]
    ],
        columns=['input_1', 'input_2', 'output', 'discovered'])
    return title, description, elements, recipes


def placeholder_checker():
    return True
