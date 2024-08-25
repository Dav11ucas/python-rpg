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
                print('\n\n\nDISTRIBUTE YOUR POINTS')
                atkp = int(input('ATKP = '))
                hp = int(input('HP = '))
                ap = int(input('AP = '))
                sum = ap + hp + atkp
                if hp > 0 and ap > 0 and atkp > 0:
                    if sum == 100:
                        break
                    else:
                        print('ERROR: the sum of values need to be equal to 100')
                else:
                    print('ERROR: the values need to be positive')
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
            item = ['hp potion', 'lv potion']
        elif merchant_type == 'blacksmith':
            item = ['sword', 'armor'] 

        merchant_dictionary = {
            'event_type': 'merchant',
            'name': merchant_name + ' the ' + merchant_type,
            'type': merchant_type,
            'items': item
        }

        event_list.append(merchant_dictionary)

        #gera um mercador e logo após o adiciona a lista de eventos.

    def treasure_generator_event():
        treasure_type = ['power potion', 'strengh potion', 'hp potion', 'sandwich']
        

#objects
player = player_class()
events = events_class()

#game
os.system('cls')
player.character_creation()

for i in range(10):
    events.monster_generator_event()
    events.mercharnt_generator_event()
    random.shuffle(event_list)
    #transformar essa ação em uma função de gerar eventos.

for current_event in event_list:
    if current_event['event_type'] == 'monster':
        os.system('cls')
        print(f'you found a {current_event['name']}, level: {current_event['level']}') 
        try:
            action = int(input('type 1 to continue, [any key] to stop: '))
        except:
            print('you must type an number')
        if action != 1:
            break
        else:
            os.system('cls')
            print(f'{current_event['name']}')
            print(f'level: {current_event['level']}')
            print(f'atkp: {current_event['atkp']}')
            print(f'hp: {current_event['hp']}')
            print('\n1 to atack')
            while True:
                try:
                    action = int(input('>'))
                except:
                    print('you must type a number')
                if action == 1:
                    current_event['hp'] -= atkp
                    hp -= current_event['atkp']
                    print(f'\n{current_event['name']} hp:{current_event['hp']}') 
                    print(f'{player_name} hp:{hp}')
                    if hp <= 0:
                        print('YOU DIED')
                        action = input('>')
                        break
                else:
                    break
    elif current_event['event_type'] == 'merchant':
        os.system('cls')
        print(f'you found a {current_event['name']}')
        action = int(input('type 1 to continue, [any key] to stop: '))
        if action != 1:
            break