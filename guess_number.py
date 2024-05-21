import numpy as np

random_num = np.random.randint(0,100)
count = 0
while True:
        guess =  input('Guess the number:')
        if guess.isdigit():
            count+=1
            num = int(guess)
            if num == random_num:
                print(f'You guessed it right! its {random_num}')
                print(f'You guessed the right number in {count}th attempt')
                break
            else:
                print('Wrong guess! Try again')
                if num < random_num:
                    print('your guess is lower')
                if num > random_num:
                    print('your guess is higher')
        else:
            print('wrong input,please enter again')
