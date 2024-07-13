import math
import random

npc_list = []
level = random.randint(0, 100)

#player stats
player_level = 0

def create_monster():
    name_list = ['lobo', 'troll', 'skeleton', 'cyclop']
    name = random.choice(name_list)

    new_monster = {
        "nome": f"{name} level#{level}",
        "level": level,
        "hp": 9 * level,
        "xp": math.floor(level / 3)
    }

    npc_list.append(new_monster)

def create_merchant():
    type_list = ['Black Mage', 'Warrior', 'Student', 'Monk', 'golden']
    name_list = ['Xiao', 'Ji', 'Nameless', 'Temujin', 'Vladmir', 'Kazan']

    name = random.choice(name_list) + ' the ' + random.choice(type_list)
    type = random.choice(type_list)

    if type == 'Warrior' or 'golden':
        item = ['sword',' hp potion']
    elif type == 'Monk' or 'Student':
        item = ['sacred botle']
    elif type == 'Black Mage':
        item = ['roten potion', 'hp potion']
    
    new_merchant = {
        "nome": f"{name} level#{level}",
        "type": type,
        "level": level,
        "items": item,
    }

    npc_list.append(new_merchant)

def create_place():
    name_list = ['swamp', 'cave', 'mine']
    place_name = random.choice(name_list)

    return place_name

#character creation

player_name = input('How is you called? ')
print('-'*10)
print('''
      
    Warrior - Endure the battlefield
      10 hp / 5 damage / speed 0
      
    Mage - Use your knoledge
      5 hp / 7 damage / speed 3
      
    Cursed - You have no choice but the destiny
      7 hp / 5 damage / speed 4
      
''')
print('-'*10)
while True:
    player_class = input('What class will you chose? ')
    if player_class == 'warrior':
        player_hp = 10
        player_damage = 5
        speed = 0
        break
    elif player_class == 'mage':
        player_hp = 5
        player_damage = 7
        speed = 3
        break
    elif player_class == 'cursed':
        player_hp = 7
        player_damage = 5
        speed = 4
        break
    else:
        print('This class do not exist')

#the game

for n in range (0,50):
    create_monster()
    create_merchant()

random.shuffle(npc_list)

place = create_place()

print('-'*10)
print(f'You have entered a {place}')
print('-'*10)

for index, npc in enumerate(npc_list):
    print('-'*10)
    print(f'room number: {index + 1}')
    print(f'you have encountered a {npc}')
    print('-'*10)
    action = input('what will you do? ')
    if action == 'leave':
        break