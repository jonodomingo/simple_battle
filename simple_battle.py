# Storing variables as individual items:
# player_name = 'Manuel' NOTE: Stored as a string. 
# player_attack = 10     NOTE: Can be stored or printed as float?
# player_heal = 16
# health = 100

# Storing variables in a list:
# player = ['Manuel', 10, 16, 100]

game_running = True # Variable determining wether the game is still
                    # active. 

# While the game should be running (while user wants to keep fighting):
while game_running == True:

    # Variable to determine if player wants to keep fighting:
    new_round = True

    # Storing variables in a dictionary, note the key-value pairs:
    player = {'name': 'Manuel', 'attack': 10, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack': 12, 'health': 100}  

    print('---' * 7)             # Separator.
    print('Enter Player name')   # Prompt for player name.
    player['name'] = input()     # Replace player name.

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    # While the player wants to keep fighting:
    while new_round == True:

        # Initialize local variables for player or monster wins.
        player_won = False
        monster_won = False

        # Prompt the user for an action.
        print('---' * 7)   
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        # Store the user's action in a variable.
        player_choice = input()

        # If-statements based on the player's input that print the
        # selected action:
        if player_choice == '1': 

            # Calculate new monster based on subtraction from attack,
            # then print out the new monster's health:
            monster['health'] = monster['health'] - player['attack']

            # If the monster died, end the game:
            if monster['health'] <= 0: player_won = True 
            
            # Else, monster alive, allow monster to attack.
            else: player['health'] = player['health'] - monster['attack']

            # If the player died, end the game:
            if player['health'] <= 0: monster_won = True

            # Show the user monster/player health after attacks.
            print(monster['health'])
            print(player['health'])

        elif player_choice == '2': print('Heal player')

        elif player_choice == '3': 
            new_round = False
            game_running = False

        else: print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' health')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health')

        elif player_won:
            print(player['name'] + ' won')
            new_round = False

        elif monster_won:
            print(monster['name'] + ' won')
            new_round = False