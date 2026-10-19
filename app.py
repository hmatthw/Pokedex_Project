import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[0]) """

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

""" for i in range(len(data)):
    print(data[i]['name']['english']) """

# Add a language choice feature and print the pokemons name based on the user input

""" choose = input("Which language would you like to print? ENG / JAP / CHI / FRE ").lower()
for i in range(len(data)):
    if choose == "eng":
        print(data[i]['name']['english'])
    elif choose == "jap":
        print(data[i]['name']['japanese'])
    elif choose == "chi":
        print(data[i]['name']['chinese'])
    elif choose == "fre":
        print(data[i]['name']['french'])
    else:
        print("Unaccepted language") """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

""" def type():
    typeask = input("Enter a pokemon type: ").title()
    typelist = []
    for i in range(len(data)):
        if typeask in data[i]["type"]:
            typelist.append(data[i]['name']['english'])
    if len(typelist) == 0:
        print("There is no pokemon that has this type...")
    print(typelist)
type() """


#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

