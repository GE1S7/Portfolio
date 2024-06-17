import art

#CLASSES

    
class Item:
    def __init__(self, name, pickable):
        self.name = name
        self.pickable = pickable #bool

class Node:
    # location
    def __init__(self, name, description, items, characters, directions):
        self.name = name
        self.description = description
        self.directions = directions
        self.items = items
        self.chracters = characters

    def describe(self):
        """provides a description of player's surroundings"""
        print(self.description)

class Player:
    def __init__(self, health, node, inventory):
        self.node = node
        self.inventory = inventory
        self.health = health


    # methods

    def move(self, direction):
        player.node = player.node.directions[direction]
    
    def pick_up(self, item):
        if item in self.node.items.keys():
            if self.node.items[item] == True:
                player.inventory.append(item)
                del self.node.items[item]
            else:
                print("I can't pick this up!")
        else: 
            print(f"I don't see any {item} around here...")

    def use(self):
        pass


#Items


#LOCATIONS
# dark aley
dark_alley_description = """
You stand in the dark alley.
There's a suspicious looking
fellow who's whistling while
leaning against the wall.
"""



tavern = Node(name = 'tavern', description = 'blahblahblah', items = {'nocnik':True}, characters = ['inkeeper'] , directions = {})
# tavern

dark_alley = Node(name = 'dark alley', description = dark_alley_description, items = {}, characters = ['mysterious man'], directions = {})

#map --  a dictionary of dictionaries {node1:{direction1:node2, direction2:node2 ... } ...}

map = {dark_alley:{'west':tavern},
       tavern:{'east':dark_alley}}

for i in map.keys():
    i.directions = map[i]

player = Player(health = 100, node = dark_alley, inventory = [])


# print title and intro
title = 'Wizard'

intro = """Your subjective experience slowly boots up from the utter
blackness and slowly gives in to a regular gray scale blank that you 
usually see under your closed eyes until a sudden storm of grainy 
shapes starts overflowing your field of view. While the ilussory 
privilege ofincorporeality that accompanies the blackout begins wearing 
off a dull pain starts buzzing through your head as if it was hit with a 
bludgeon. You open your eyes. After a while an opaque redness starts 
giving way to the shapes of the objects that surround you.
"""
print(art.text2art(title))

print(intro)

while True:
    print(player.node)
    command = input("> ").lower().strip()
    if command == 'quit': 
        break
    
    if command == 'help':
        print('')

    # getting to know the location

    if command == 'where am i':
        print(f'Your location: {player.node.name}.')

    if command == 'describe':
        player.node.describe()

    # acting on stuff in surroundings

    if command.startswith('move'):
        if command[5:] in player.node.directions.keys():
            player.move(command[5:])

    if command.startswith('pick up'):
            player.pick_up(command[8:])

print(player.node.items)
print(f'player inventory {player.inventory}')





"""
OBJECTIVES:
# enable the player to talk with people if there are any in the location
# enable the player to save and load the game
"""
