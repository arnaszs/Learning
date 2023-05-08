import random

# Possible words
words = ("kareivis", "lapas", "popierius", "akmuo", 
         "žirklės", "pelė", "kompiuteris", "ekranas", "laukas", 
         "langas", "medis", "lempa", "žolė", "matematika", 
         "geografija", "parkeris", "pieštukas", "kiaušinis", 
         "kopūstas", "morka", "bulvė", "paprika", "bomba", 
         "kriaušė", "daržovė", "šakutė", "šaukštas", "gėlė", 
         "bitė", "šuo", "šautuvas", "tigras", "katė", "bezdžionė", 
         "dušas", "muilas", "vyras", "moteris", "gitara", "pianinas", 
         "mikrofonas", "ausinės", "mėsa", "diržas", "kelnės", 
         "šaltibarščiai", "meilė", "kalnas", "laivas", "traukinys", 
         "kartuvės", "žaidimas", "pinigai", "kiaulė", "arklys", 
         "karvė", "barsukas", "vagis", "policininkas", "jūra", 
         "kriauklė", "vonia", "programavimas", "programuotojas", 
         "kobra", "angis", "kuprinė", "sąsiuvinis", "trintukas", "penalas")

# Choose a random word
chosen_word = random.choice(words)

# List to store guessed letters
letter_guesses = []

# Number of guesses
how_much_guesses = 13

# Infinite loop until the player guesses the word or runs out of guesses
while True:
    # Show the word with blanks for unguessed letters
    show = ''
    for letter in chosen_word:
        if letter in letter_guesses:
            show += letter
        else:
            show += '_ '
    print(show)
    
    # Ask the player to guess a letter
    guess = input('Your guess: ')
    
    # Check if the letter has already been guessed
    if guess in letter_guesses:
        print('You already guessed that letter!')
        continue
        
    # Add the guessed letter to the list of guessed letters
    letter_guesses.append(guess)
    
    # Check if the guessed letter is in the word
    if guess in chosen_word:
        print('You guessed a letter!')
    else:
        how_much_guesses -= 1
        print(f'Your guess is wrong! You have {how_much_guesses} left!')
    
    # Check if the player has guessed the whole word
    if set(chosen_word) <= set(letter_guesses):
        print('Congratulations, you guessed the word!')
        break
        
    # Check if the player has run out of guesses
    if how_much_guesses == 0:
        print(f'You have no guesses left! The word was: {chosen_word}')
