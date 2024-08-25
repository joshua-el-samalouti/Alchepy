import re
import sys
import warnings
from module import *


# TODO: Debug prints
def start_module(path: str):
    warnings.filterwarnings("ignore")
    module = Module(path)
    print(module.title, "\n")
    print(module.introduction)
    while True:
        command = input()
        keyword = re.search(r'\S+', command).group().strip()
        argument = re.search(f'(?<={keyword}\s)\S.*', command)
        if argument:
            argument = argument.group().strip()
        try:
            data = {'add': add,
                    'info': module_info,
                    'quit': quit_app,
                    'help': helper,
                    'list': list_group,
                    'groups': groups,
                    'options': options,
                    'stats': stats,
                    'debug': debugger}[keyword](argument, module)
        except KeyError:
            print("invalid command")
    pass


def quit_app(argument, module):
    sys.exit()


def module_info(argument, module):
    print(module.info)


def helper(argument, module):
    print("WIP")


def stats(argument, module):
    print('WIP')


def options(argument, module):
    print('WIP')


def groups(argument, module):
    print('Groups:\n')
    for group in module.get_unlocked_groups():
        print(group)


def list_group(argument, module):
    if argument in module.get_unlocked_groups():
        print(f'\n{argument}:\n')
        for element in module.elements.loc[module.elements[2]].loc[module.elements[1] == argument][0]:
            print(element)
    else:
        print(argument, " is an invalid group")


def debugger(argument, module):
    module.toggle_debug()
    if module.debug_mode:
        print("debug mode activated")
    else:
        print("debug mode deactivated")


def add(argument, module):
    input_elements = re.split(r'\s\+\s', argument)
    input_elements = [element.strip() for element in input_elements]
    if len(input_elements) != 2:
        print("wrong number of elements")
    result_info = module.match_elements(input_elements[0], input_elements[1])
    match result_info[0]:
        case -1:
            print("One or more elements are invalid")
        case 0:
            print("Nothing happened")
        case 1:
            recipe = module.get_recipe(result_info[1])
            print(recipe[0], ' + ', recipe[1], ' = ', recipe[2])
        case 2:
            recipe = module.get_recipe(result_info[1])
            print(recipe[0], ' + ', recipe[1], ' = ', recipe[2])
        case 3:
            recipe = module.get_recipe(result_info[1])
            for element in recipe[3]:
                print('*NEW ELEMENT UNLOCKED: ', element[3])
            print(recipe[0], ' + ', recipe[1], ' = ', recipe[2])
    pass
