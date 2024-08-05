import random
import os
import math

#general variables
event_list = [] #engloba todos os eventos que vão ocorrer em sequência durante o jogo

#player variables
player_name = ""
atkp = 0
hp = 0
ap = 0
player_lv = 1


class player_class:
    def character_creation(self):

        print('''

        For now on you will need to distribute your points, you start with 10

        distribute it wrong will lead you to repeat the process

        Atack points -> ATKP
        Health points -> HP
        Agility points -> AP
        ''')
        while True:
            try:
                atkp = int(input('ATKP = '))
                hp = int(input('HP = '))
                ap = int(input('AP = '))
                sum = ap + hp + + atkp
                if sum == 10:
                    break
                else:
                    print('the sum of values need to be equal to 10')
            except:
                print("it's necessary that you write a number")
    
        player_name = input('type the name of your character: ')

class events_class:
    def monster_generator_event(self):
        #change it for a .json file
        monster_name_list = ['wolf', 'skeleton', 'goblin', 'zombie']
        monster_name = random.choice(monster_name_list)
        monster_level = random.randint(player_lv, player_lv + 10)
        monster_atkp = monster_level - 2
        monster_hp = monster_level

        monster_dictionary = {
            'event_type': 'monster',
            'name': monster_name,
            'level': monster_level,
            'atkp': monster_atkp,
            'hp': monster_hp
        }

        event_list.append(monster_dictionary)

        #gera um monstro e add ele a lista de eventos

    def mercharnt_generator_event(self):
        merchant_name_list = ['Siren', 'Wu', 'Garuda', 'Naib']
        merchant_name = random.choice(merchant_name_list)
        merchant_type_list = ['alquimist', 'blacksmith']
        merchant_type = random.choice(merchant_type_list)

        if merchant_type == 'alquimist':
            item = ['hp_potion', 'lv_potion']
        elif merchant_type == 'blacksmith':
            item = ['sword', 'armor'] 

        merchant_dictionary = {
            'event_type': 'merchant',
            'name': merchant_name + 'the' + merchant_type,
            'type': merchant_type,
            'items': item
        }

        event_list.append(merchant_dictionary)

        #gera um mercador e logo após o adiciona a lista de eventos.
    
#objects
player = player_class()
events = events_class()

#game
player.character_creation()

for i in range(10):
    events.monster_generator_event()
    events.mercharnt_generator_event()
    #talvez transformar essa ação em uma função de gerar eventos.

for current_event in event_list:
    print(current_event)
    action = input('type 1 to continue, 2 to stop')
    if action == 2:
        break