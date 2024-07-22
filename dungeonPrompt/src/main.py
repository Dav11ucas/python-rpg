import os
import NpcCreator
import random

os.system('cls')
print('''
      _                                                                    _   
     | |                                                                  | |  
   __| |_   _ _ __   __ _  ___  ___  _ __  _ __  _ __ ___  _ __ ___  _ __ | |_ 
  / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \| '_ \| '__/ _ \| '_ ` _ \| '_ \| __|
 | (_| | |_| | | | | (_| |  __/ (_) | | | | |_) | | | (_) | | | | | | |_) | |_ 
  \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_| .__/|_|  \___/|_| |_| |_| .__/ \__|
                     __/ |                | |                       | |        
                    |___/                 |_|                       |_|
      ''')
start = input('''
              
Wellcome to the game, type anything to begin
              
>''')
os.system('cls')

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
    
os.system('cls')

#the game

for n in range (0,50):
    create_monster()
    create_merchant()

random.shuffle(npc_list)

place = create_place()

print('-'*10)
print(f'You have entered a {place}')
print('-'*10)
start = input('input anything to continue')
os.system('cls')
for index, NpcCreator in enumerate(npc_list):
    if NpcCreator['npc_type'] == 'monster':
        print('-'*10)
        print(f'place: {place}')
        print(f'room number: {index + 1}')
        print(f'you have encountered a monster')
        print('-'*10)
        print(f'{NpcCreator['name']}')
        print('-'*10)
        action = input('what will you do? [1- run | 2- atack | 3- inventory]')
        os.system('cls')
        if action == 'leave':
            break
        elif action == '1':
            dice = random.randint(0, 100)
            if dice >= NpcCreator['level']:
                print('you did run')
            else:
                print('You failed to run')
                print('-'*10)
                print(f'place: {place}')
                print(f'room number: {index + 1}')
                print(f'you have encountered a monster')
                print('-'*10)
                print(f'{NpcCreator['name']}')
                print('-'*10)
                action = input('what will you do? [2- atack | 3- inventory]')
                os.system('cls')
    elif NpcCreator['npc_type'] == 'merchant':
        print('-'*10)
        print(f'place: {place}')
        print(f'room number: {index + 1}')
        print(f'you have encountered a merchant')
        print('-'*10)
        print(f'''
name: {NpcCreator['name']}

items: {NpcCreator['items']}
''')
        print('-'*10)
        action = input('what will you do? [1- leave | 2- buy | 3- inventory]')
        os.system('cls')
        if action == 'leave':
            break

        #solve the item problem