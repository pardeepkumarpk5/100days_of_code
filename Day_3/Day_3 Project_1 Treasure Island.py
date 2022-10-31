print('Welcome to the treasure island')

# first choice
choice_1 = input(
    'You\'re at cross road. Where you want to go? Type "left" or "right" \n')

if choice_1 == 'left':
    choice_2 = input(
        'You come to a lake. There is an island in the middle of the lake. \n Type "wait" to wait for a boat. Type "swim" to swim across \n')

    if choice_2 == 'wait':
        choice_3 = input(
            'You arrived at the island unharmed. There is a house with 3 doors. \n One "red" , one "yellow" and one "blue". Which color do you choose? \n')

        if choice_3 == 'blue':
            print('Congratulations You win.')
        else:
            print('Game over.')

    else:
        print('Game over.')

else:
    print('Game Over.')
