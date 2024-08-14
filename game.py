import re
import sys
import warnings
from placeholder import *
import localization as loc
import options as opt
import debug


def new_game():
    if not opt.warnings:
        warnings.filterwarnings("ignore")
    lang = lang_select()
    # TODO: Add Module Select Here
    data = loader('placeholder', lang)
    print(data['title'])
    print(data['description'])

    while True:
        command = input()
        keyword = re.search(r'\S+', command).group().strip()
        argument = re.search(f'(?<={keyword}\s)\S.*', command)
        if argument:
            argument = argument.group().strip()
        try:
            data = {'add': add,
                    'info': info,
                    'quit': quit_app,
                    'help': helper,
                    'list': list_group,
                    'groups': groups,
                    'options': options,
                    'stats': stats,
                    'debug': debugger}[keyword](argument, data, lang)
        except KeyError:
            print(loc.invalid_command[lang])

    pass


def loader(module, lang):
    return placeholder_loader(lang)


def checker():
    return placeholder_checker()


def add(argument, data, lang):
    input_elements = re.split(r'\s\+\s', argument)
    input_elements = [element.strip() for element in input_elements]
    if len(input_elements) < 2:
        print(loc.too_little_elements[lang])
    elif len(input_elements) == 2:
        if not has_elements(input_elements, data):
            print(loc.invalid_element[lang])
            return data
        # returns subset of recipes dataframe matching input elements. This should always be 0 or 1
        # In case of 0 it tries again with inputs switched.
        match = data['recipes'][data['recipes']['input_1'] == input_elements[0]] \
            [data['recipes']['input_2'] == input_elements[1]]
        if len(match) == 1:
            first = 'input_1'
            second = 'input_2'
        if len(match) == 0:
            match = data['recipes'][data['recipes']['input_1'] == input_elements[1]] \
                [data['recipes']['input_2'] == input_elements[0]]
            if len(match) == 1:
                first = 'input_2'
                second = 'input_1'
        if len(match) == 1:
            if match['discovered'][0] and opt.disable_discovered_combinations:
                print(loc.nothing_happened[lang])
            else:
                if not match['discovered'][0]:
                    print('*', loc.new_combination[lang], '*')
                print(f'{match["input_1"][0]} + {match["input_2"][0]} = {match["output"][0]}')
                temp_recipes = data['recipes']
                temp_recipes.loc[(data['recipes'][first] == input_elements[0]) &
                                 (data['recipes'][second] == input_elements[1]), 'discovered'] = True
                temp_elements = data['elements']
                for element in match['output'][0]:
                    temp_elements.loc[data['elements']['name'] == element, 'unlocked'] = True
                data['recipes'] = temp_recipes
                data['elements'] = temp_elements
        if len(match) == 0:
            print(loc.nothing_happened[lang])
    elif len(input_elements) > 2:
        print(loc.too_many_elements[lang])
    return data


def info(argument, data, lang):
    print(data['info'])
    return data


def options(argument, data, lang):
    print('WIP')
    return data


def quit_app(argument, data, lang):
    sys.exit()


def helper(argument, data, lang):
    print(loc.help_menu[lang])
    return data


def list_group(argument, data, lang):
    if argument in unlocked_groups(data):
        print(f'\n{argument}:\n')
        for element in data['elements'].loc[data['elements']['unlocked']].loc[data['elements']['group'] == argument][
            'name']:
            print(element)
    else:
        print(argument)
        print("Invalid group")
    return data


def stats(argument, data, lang):
    print('WIP')
    return data


def groups(argument, data, lang):
    print(loc.groups[lang], '\n')
    for group in unlocked_groups(data):
        print(group)
    return data


def lang_select():
    print('\nSelect language:\n')
    for element in loc.available_languages:
        print(element[0], ': ', element[1])
    while True:
        selection = input()
        if selection in [lang[1] for lang in loc.available_languages]:
            return selection
        else:
            print('Invalid selection')


def unlocked_groups(data):
    return data['elements'].loc[data['elements']['unlocked']]['group'].unique()


def has_elements(elements, data):
    selection = data['elements'].loc[data['elements']['unlocked']]['name']
    for element in elements:
        if element not in selection.values:
            return False
    return True


def debugger(argument, data, lang):
    if opt.debug_mode:
        print('WIP')
    else:
        print(loc.debug_disabled[lang])
    return data
