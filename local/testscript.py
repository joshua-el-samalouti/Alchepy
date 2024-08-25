import alchlib

path = "C:/Users/joshu/Documents/Github/alchemy-modules/Covers/doodle_mafia.json"
doodle_mafia = alchlib.Module(path)
doodle_mafia.toggle_debug()

x = doodle_mafia.find_recipe("crime", "crime")
print(x)
