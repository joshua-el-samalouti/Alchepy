import re
import sys
from placeholder import *
import localization as loc


def new_game():
    for element in loc.available_languages:
        print(element[0], ': ', element[1])
    lang = input()
    # Add Module Select Here
    title, description, elements, recipes = loader('placeholder', lang)
    print(title)
    print(description)

    while True:
        command = input()
        keyword = re.search('\S+', command).group().strip()
        expression = re.search(f'(?<={keyword}\s)\S.*', command).group().strip()
        print(keyword)
        try:
            {'add': add,
             'info': info,
             'quit': quit_app}[keyword](expression)
        except KeyError:
            print('Invalid command')

    pass


def loader(module, lang):
    return placeholder_loader(lang)


def checker():
    return placeholder_checker()


def add(expression):
    print('add')
    print(expression)


def info(expression):
    print('info')


def quit_app(expression):
    sys.exit()
