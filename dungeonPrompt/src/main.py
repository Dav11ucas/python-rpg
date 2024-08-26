import json
import os

with open('dungeonPrompt/src/classes.json', 'r') as classesfile:
    classes_data = json.load(classesfile)
with open('dungeonPrompt/src/classes.json', 'r') as enemyfile:
    enemy_data = json.load(enemyfile)
 
def character_creation():
    character_name_length = 10
    print('CHARACTER CREATION')

    while True:
        character_name = input(f'Type your character name (up to {character_name_length} characters): ')
        if len(character_name) <= character_name_length:
            break
        else:
            print(f'Please enter a name with less than {character_name_length} characters.')

    print('These are all classes:')
    class_names = [character_class['name'] for character_class in classes_data]
    for i, name in enumerate(class_names):
        print(f'{i+1}. {name}')

    while True:
        character_class_index = input('Select your character class (by number): ')
        try:
            character_class_index = int(character_class_index) - 1
            if 0 <= character_class_index < len(classes_data):
                break
            else:
                print('Invalid class selection. Please choose a number from the list.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    chosen_class = classes_data[character_class_index]
    print(f'\nCongratulations, {character_name}! You chose the {chosen_class["name"]} class.')

def enemy_generator():
    enemy_names = [enemys['name'] for enemys in enemy_data]
    enemy_damage = [enemys['damage'] for enemys in enemy_data]
    enemy_health = [enemys['health'] for enemys in enemy_data]
    


character_creation()
enemy_generator()