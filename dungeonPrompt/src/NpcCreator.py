import math
import random
import os

def create_monster():
    name_list = ['lobo', 'troll', 'skeleton', 'cyclop']
    name = random.choice(name_list)

    new_monster = {
        "npc_type": 'monster',
        "name": f"{name} level#{level}",
        "level": level,
        "hp": 9 * level,
        "xp": math.floor(level / 3)
    }

    npc_list.append(new_monster)

def create_merchant():
    type_list = ['Black Mage', 'Warrior', 'Student', 'Monk', 'golden']
    name_list = ['Xiao', 'Ji', 'Nameless', 'Temujin', 'Vladmir', 'Kazan']
    item = []

    name = random.choice(name_list) + ' the ' + random.choice(type_list)
    type = random.choice(type_list)

    if type == 'Warrior' or type == 'golden':
        item = ['sword', 'hp potion']
    elif type == 'Monk' or type == 'Student':
        item = ['sacred bottle']
    elif type == 'Black Mage':
        item = ['rotten potion', 'hp potion']
    else:
        item = []

    
    new_merchant = {
        "npc_type": 'merchant',
        "name": f"{name} level#{level}",
        "type": type,
        "level": level,
        "items": item,
    }

    npc_list.append(new_merchant)

def create_place():
    name_list = ['swamp', 'cave', 'mine']
    place_name = random.choice(name_list)

    return place_name
