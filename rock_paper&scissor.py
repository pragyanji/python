import random
lst1 = ['ROCK','PAPER','SCISSOR']
while True:
    print('Lets play:')
    turn1 = random.choice(lst1)
    turn2 = input('\nYour turn:')
    turn2 = turn2.upper()
    if turn1 == turn2:
        print('Its a draw')
    elif turn1 == 'ROCK' and turn2 == 'SCISSOR' or turn1 == 'SCISSOR' and turn2 == 'PAPER' or turn1 == 'PAPER' and turn2 == 'ROCK':
        print('You lose')
        break
    elif turn1 == 'ROCK' and turn2 == 'PAPER' or turn1 == 'SCISSOR' and turn2 == 'ROCK' or turn1 == 'PAPER' and turn2 == 'SCISSOR':
        print('You win')
        break
    else:
        print('invalid input')