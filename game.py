import re
import sys
from placeholder import *
import localization as loc


def new_game():
    lang = lang_select()
    # Add Module Select Here
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
                    'stats': stats}[keyword](argument, data, lang)
        except KeyError:
            print('Invalid command')

    pass


def loader(module, lang):
    return placeholder_loader(lang)


def checker():
    return placeholder_checker()


def add(argument, data, lang):
    print('WIP')
    return data


def info(argument, data, lang):
    print(data['info'])
    return data


def quit_app(argument, data, lang):
    sys.exit()


def helper(argument, data, lang):
    print(loc.help_menu[lang])
    return data


def list_group(argument, data, lang):
    if argument in unlocked_groups(data):
        print(f'\n{argument}:\n')
        for element in data['elements'].loc[data['elements']['unlocked']].loc[data['elements']['group'] == argument]['name']:
            print(element)
    else:
        print(argument)
        print("Invalid group")
    return data


def stats(argument, data, lang):
    print('WIP')
    return data


def groups(argument, data, lang):
    print('Groups:\n')
    for group in unlocked_groups(data):
        print(group)
    return data


def lang_select():
    for element in loc.available_languages:
        print(element[0], ': ', element[1])
    while True:
        selection = input()
        if selection in [lang[1] for lang in loc.available_languages]:
            return selection
        else:
            print('invalid selection')


def unlocked_groups(data):
    return data['elements'].loc[data['elements']['unlocked']]['group'].unique()
