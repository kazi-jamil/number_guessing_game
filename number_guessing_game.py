import random

secret_number = random.randint(1,20)
attempts = 0
max_attempts = 5

print('!! Welcome to the Number Guessing Game !!')
print('you have to guess a No. between 1-20')
print('only 5 attempts left')
print()

while attempts < max_attempts:
    guess = int(input('take a guess: '))
    attempts += 1
    if guess < secret_number:
        print('Too low, try again.')
        print(f'you have used {attempts}/{max_attempts} tries')
        print()
    elif guess > secret_number:
        print('Too high, try again.')
        print(f'you have used {attempts}/{max_attempts} tries')
        print()
    else:
        print(f'!! Congo, You got it in {attempts} tries !!')
        break
    if attempts >= max_attempts:
        print(f'You have used all {max_attempts} tries')
        print(f'The number was {secret_number}')
        break


