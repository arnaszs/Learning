import random
import string
                                                ## THE NUMBER GUESSING GAME
# def guess(num):
#     random_number = random.randint(1, num)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a random number between 1 and {num}: '))
#         if guess > num:
#             print('Sorry, you guessed too high')
#         elif guess < num:
#             print('Sorry you guessed too low')
#         else:
#             print(f'Congratulations you guessed the number {num}')
#             break
# guess(10)
                                                ## THE COMPUTER NUMBER GUESSING GAME
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         guess = random.randint(low, high)
#         feedback = input(f'If {guess} is too high (H), if guess is too low (L), if guess is correct (C)').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#         else:
#             print(f'Congratulations the computer guessed the number {guess} correctly!')

# computer_guess(1000)



words = ('sword', 'giraffe', 'basketball', 'unicorn', 'foot', 'famlit', 'sunshine')

def hangman():
    word_letters = [x for x in random.choice(words).upper()]
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        user_letter = input('Guess a letter: ').upper()
        print('You have used these letters, ' ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word_letters]
        print('current word, ', ' '.join(word_list))

        if user_letter in alphabet - used_letters:
            print(used_letters)
            print(word_list)
            print(word_letters)
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print('You already guessed this letter, try another one')
        else:
            print('The program doesn\'t allow this letter. try again.')


hangman()




