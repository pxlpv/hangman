import random

words = ['horse', 'train', 'country', 'water', 'steak']

print('Welcome to hangman!')

wrong_guesses = 0
guesses = []
word = words[random.randint(0, len(words) - 1)].upper()
censored = ['_'] * len(word)

while (wrong_guesses < 5):
    print(f'\nGuesses: {guesses}')
    print(f'Wrong Guesses: {wrong_guesses}/5')
    print(' '.join(censored))

    if '_' in censored:
        guess = input('Please enter a letter to guess: ').upper()
        if guess.isalpha():
            if (guess in word) & (guess not in guesses):
                guesses.append(guess)
                print('--> YAY! Thats a correct letter!')
                for i in range(len(word)):
                    if word[i] == guess:
                        censored[i] = guess
            elif guess in guesses:
                print('--> Youve already guessed that letter. Please try again.')
            else:
                wrong_guesses += 1
                guesses.append(guess)
                print('--> Sorry! Thats not a correct guess!')
        else:
            print('Invalid input. Please enter a letter.')
            pass
    else:
        break

if wrong_guesses < 5:
    print('You win!')
else:
    print('You lost!')