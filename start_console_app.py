import alchlib.console_app

path_desktop = "C:/Users/joshu/Documents/Github/alchemy-modules/Covers/doodle_mafia.json"
path_laptop = "C:/Users/maeba/OneDrive/Desktop/Alchemy Modules/alchemy-modules/Covers/doodle_mafia.json"
print("please enter the path of the module (json file) you want to play:")
path = input()
alchlib.console_app.start_module(path)
