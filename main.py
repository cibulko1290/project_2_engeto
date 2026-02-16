'''
Project_2: The second project from Engeto Academie - Bulls and Cows game
Author: Lucia Luptakova
email: lucy.luptakova@gmail.com
'''

delimiter = '-' * 46
print (f'''Hi there! \n{delimiter} \nI've generated a random 4 digit number for you.
Let's play the Bulls and Cows game. \n{delimiter} \nEnter a number: \n{delimiter}''')

import random
import time

def generate_secret_number():
    first = random.choice(range(1,10))
    other = random.sample([n for n in range(10) if n != first], 3)
    return str(first) + ''.join(map(str, other))

def validate_guess(guess):
    '''
    Validate the user's guess for the Bulls and Cows game.
    Checks:
    - lenght must be 4 digits
    - must contain only numbers
    - cannot start with zero
    - digits must not repeat
    :param guess: type str: The user's guess.
    Returns:
    - tuple (bool, str) - bool indicates validity and str contains an error message.
    '''
    if len(guess) != 4:
        return False, 'Sorry, the number must be 4 digits long.\nEnter a valid 4 digit number.'
    if not guess.isdigit():
        return False, 'Sorry, the number must contain only digits.\nEnter a valid 4 digit number.'
    if guess[0] == '0':
        return False, 'Sorry, the number cannot start with 0.\nEnter a valid 4 digit number.'
    if len(set(guess)) != 4:
        return False, 'Sorry, the numbers cannot be repeated.\nEnter a valid 4 digit number.'
    return True, ''

def count_cows_and_bulls(secret, guess):
    '''
    Calculate number of cows and bulls for a guess.
    Bulls = correct digit in the correct position.
    Cows = correct digit in the wrong position.    
    :param secret: type str: The generated secret 4-digit number.
    :param guess: type str: The user's guess.
    Returns:
    tuple: (cows, bulls)
    '''
    matches = len(set(secret) & set(guess))
    bulls = sum(1 for g, s in zip(guess, secret) if g == s)
    cows = matches - bulls
    return cows, bulls

def plural(word, count):
    return word if count == 1 else word + 's'

def print_result(cows, bulls):
    cow_word = plural('cow', cows)
    bull_word = plural('bull', bulls)
    print(f'{cows} {cow_word}, {bulls} {bull_word}')

def play_game(secret):
    '''
    Run the main game loop.
    Repeatedly asks the user for guesses until the  secret number is guessed.
    Displays cows and bulls count after each valid guess.
    :param secret: type str: The generated secret 4-digit number.
    returns: 
    tuple: (attempts, elapsed_time) - number of attempts and time taken to guess the number.
    '''
    attempts = 0
    start_time = time.time()
    
    while True:
        print (delimiter)
        guess = input('>>> ')
        valid, message = validate_guess(guess)
        
        if not valid:
            print (message)
            continue

        attempts += 1
        cows, bulls = count_cows_and_bulls(secret, guess)
            
        if bulls == 4:
                end_time = time.time()
                elapsed_time = end_time - start_time

                print(f'''Correct, you\'ve guessed the right number \nin {attempts} attempts.
{delimiter}\nThat\'s amazing!''')                
                print(f'Elapsed time: {elapsed_time:.2f} seconds\n{delimiter}')
            
                return attempts, elapsed_time
        else:
            print_result(cows, bulls)

statistics = []

while True:
    secret = generate_secret_number()
    attempts, elapsed_time = play_game(secret)
    
    statistics.append({
        'attempts': attempts,
        'time': elapsed_time
    })
    
    answer = input('Do you want to play again? (y/n): ').lower()
    
    if answer != 'y':
        break

print(f'{delimiter} \nGame statistics \n{delimiter}')
for i, stat in enumerate(statistics, 1):
    print(f'Game {i}: {stat["attempts"]} attempts, {stat["time"]:.2f} seconds')
