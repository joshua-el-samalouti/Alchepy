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
        keyword = re.search('\S+', command).group().strip()
        expression = re.search(f'(?<={keyword}\s)\S.*', command)
        if expression:
            expression = expression.group().strip()
        try:
            data = {'add': add,
                    'info': info,
                    'quit': quit_app,
                    'help': helper,
                    'list': list_group,
                    'groups': groups,
                    'stats': stats}[keyword](expression, data, lang)
        except KeyError:
            print('Invalid command')

    pass


def loader(module, lang):
    return placeholder_loader(lang)


def checker():
    return placeholder_checker()


def add(expression, data, lang):
    print('WIP')
    return data


def info(expression, data, lang):
    print(data['info'])
    return data


def quit_app(expression, data, lang):
    sys.exit()


def helper(expression, data, lang):
    print(loc.help_menu[lang])
    return data


def list_group(expression, data, lang):
    print('WIP')
    return data


def stats(expression, data, lang):
    print('WIP')
    return data


def groups(expression, data, lang):
    print('Groups:\n')
    for group in data['elements'].loc[data['elements']['unlocked']]['group'].unique():
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

