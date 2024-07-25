import random
import os
import json

#global variables
player_hp = 0
player_damage = 0
player_scape = 0
player_dodge = 0

npc_list = []

def create_place():
    #escolher uma lista de monstros, merdadores e qualquer outra possibilidade para as salas.
    place_list = ['Swamp', 'Forest', 'Ruins', 'Cave']
    place = random.choice(place_list)
    return place

def select_npcs():
    #o loot deve ser randomico dentro de uma pequenda possibilidade de drop e não drop
    with open("data.json", "r") as f:
        monsters = json.load(f)

    place = create_place()
    monster_list = []

    if place == 'Swamp':
        monster_list.append(monsters[0])
    elif place == 'Forest':
        monster_list.append(monsters[1])
    elif place == 'Ruins':
        monster_list.append(monsters[2])
    elif place == 'Cave':
        monster_list.append(monsters[3])

#def create_merchant():
#cada mercador deve ter seus produtos, e por enquanto é isso

#def create_room():
#cada sala deve ser padronizada, mas com suas próprias pequenas especificidades para cada lugar

def create_player():
    while True:
        os.system('cls')
        print('''Atention, your initial status can only reach 10 with the sum of every items
There will be DAMAGE, HEALTH, SCAPE, and DODGE
              ''')
        try:
            player_damage = int(input('select value to your damage: '))
            player_hp = int(input('select value to your health: '))
            player_scape = int(input('select value to your scapee: '))
            player_dodge = int(input('select value to your dodge: '))
            status_sum = player_damage + player_hp + player_scape + player_dodge
            if status_sum == 10:
                break
            else:
                os.system('cls')
                print("The sum of your stats must be equal to 10.")
                accept = input()
        except ValueError:
            os.system('cls')
            print("Please enter only numbers.")
os.system('clear')

#Game

create_player()
select_npcs()