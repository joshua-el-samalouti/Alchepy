## What is Alchepy?
Alchepy is a Python library for puzzle games in the style of titles like the popular Doodle God or Little Alchemy, in which the player is given certain elements they can combine to discover other elements. Usually the goal is to discover all elements.

## What is included in Achepy
Alchepy is still in early stages of development. Currently it includes:
- A 'Module' class that can handle all the necessary database operations and can load game data from a JSON file
- A console application to test and play loaded modules

## What is an Alchepy module?
An Alchepy module is the set of data of a game environment that's handled by Alchepy. This includes all contained elements and recipes as well as metadata

## How does a module JSON file have to be structured?
The JSON file has to contain an object that contains the following attributes:
- "title": String (title of the module)
- "description": String (description of the module)
- "introduction": String (introduction text)
- "elements": Array (list of elements)
  - Arrays (individual elements)
    - String (name of the element)
    - String (name of the element's group)
    - Int (0 for locked elements, 1 for unlocked ones)
- "recipes": Array (list of recipes)
  - Arrays (individual recipes)
    - String (name of first input element)
    - String (name of second input element)
    - Array (names of output elements, currently limited to a length of 1)
      - Strings (names of output elements)
    - Int (0 for undiscovered recipes, 1 for discovered ones, will most likely always be 0)
- "options": Object
  - "symmetry": int (1 if the order of recipe input elements is to be ignored, otherwise 0)
- "info": string (information about the module)
- "version": string (version of Alchepy the module was developed for)
- "author": string (name of the module author)

## How do I use the console application? 
The console application first requires you to input the path of a module JSON file to load.
It then has the following commands (square brackets are omitted and signal variables):
#### add \[element name\] + \[element name\]
- adds any amount of elements, if the combination is valid it marks the recipe as discovered and unlocks the result elements
#### debug
- toggles debug mode on/off. Currently debug mode simply gives additional information when using commands
#### groups
- lists currently unlocked groups
#### help
- WIP command
#### info
- prints the info text of the current module
#### list \[group name\]
- lists the currently unlocked elements in an unlocked group
#### options
- WIP command
#### quit
- closes the application
#### stats
- WIP command

## What are the plans for Alchepy's future?
- A sample module to play and get a feel for the library
- Recipes with more than two input elements
- Recipes with more than one output element
- Recipe labels
- Methods to save and load progress
- Conditional events
- Additional commands for the console app
- A more detailed guide to module creation
