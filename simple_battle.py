# Storing variables as individual items:
# player_name = 'Manuel' NOTE: Stored as a string. 
# player_attack = 10     NOTE: Can be stored or printed as float?
# player_heal = 16
# health = 100

# Storing variables in a list:
# player = ['Manuel', 10, 16, 100]

# Storing variables in a dictionary, note the key-value pairs:
player = {'name': 'Manuel', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'Max', 'attack': 12, 'health': 100}

game_running = True # Variable determining wether the game is still
                    # active. 

# While the game should be running (while monster/player are still alive):
while game_running == True:

    # Initialize local variables for player or monster wins.
    player_won = False
    monster_won = False

    # Prompt the user for an action.
    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    # Store the user's action in a variable.
    player_choice = input()

    # If-statements based on the player's input that print the
    # selected action:
    if player_choice == '1': 

        # Calculate new monster based on subtraction from attack,
        # then print out the new monster's health:
        monster['health'] = monster['health'] - player['attack']

        # If the monster died, end the game:
        if monster['health'] <= 0:
            pass 
        
        # Else, monster alive, allow monster to attack.
        else:
            player['health'] = player['health'] - monster['attack']

        # If the monster died, end the game:
        if player['health'] <= 0:
            pass # Pass allows for no action.

        # Show the user monster/player health after attacks.
        print(monster['health'])
        print(player['health'])

    elif player_choice == '2': print('Heal player')
    else: print('Invalid Input')

    # CHECK to see if the game is over, noting game is over if 
    # either player is at less than or equal to zero health.
    if player['health'] <= 0 or monster['health'] <= 0:
        game_running = False
