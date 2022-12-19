    # -----------------------------------
    # Helper code
    # You don't need to understand this helper code,
    # but you will have to know how to use the functions
    # (so be sure to read the docstrings!)
    
    import random
    import string
    
    WORDLIST_FILENAME = "word_list.txt"
    '''
    returns valid words
        '''
    def secret_words():
    
        print("Reading word_list file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # word_list: list of strings
        word_list = line.split()
        print(len(word_list), "words found")
        return word_list
    
    def choose_word(word_list):
        
        
        return random.choice(word_list)
    
    # end of helper code
    # -----------------------------------
    # Load the list of words into the variable word_list
    # so that it can be accessed from anywhere in the program
    word_list = secret_words()
    '''
    word is the word that the player has to guess
    guess is the list of letters that the player has guessed so far 
    
    '''  
    def is_word_guessed(word, guessed):
       
        # FILL IN YOUR CODE HERE...
        for c in word:
            if c not in guessed:
                return False
        return True
    
    
    
    
    def get_guessed_word(word, guessed):
        
        
        # FILL IN YOUR CODE HERE...
        output = ""
        for c in word:
            if c in guessed: 
                output += c
            else:
                output += " "
        return output
    
    def get_available_letters(guessed):
      
        '''
        this returns the letters that had been guess so far
        '''
        # FILL IN YOUR CODE HERE...
        output = string.ascii_lowercase
        for c in guessed:
            output = output.replace(c, "")
        return output
    
    
    '''
     The game starts here, the start of the game the player is knows that how many letters the secret letter gets 
     along with how many guess they have
     
     after every guess it should say whether the guess is right or not 
     after ever round it should display how many words in the letter is partially correct
    '''
    def game_loop(word):
       
    # FILL IN YOUR CODE HERE...
        print ("Let the game begin!")
        print ("I am thinking of a word with", len(word), "letters")
        guess_remain = 8
        guessed = []
        while is_word_guessed(word, guessed) == False and guess_remain > 0:
            print("You have", guess_remain, "guesses remaining")
            remain_letter = get_available_letters(guessed)
            print("Letters available to you:", remain_letter)
    
            c = input("Guess a letter:").lower()
            if c in remain_letter:
                guessed.append(c)
                if c in word:
                    print("Correct:", get_guessed_word(word, guessed))
                else:
                    print("Incorrect, this letter is not in my word:", get_guessed_word(word, guessed))
                    guess_remain -= 1
            else:
                print("You fool", get_guessed_word(word, guessed))
    
        if (is_word_guessed(word, guessed)):
            print ("You WIN")
        else :
            print("GAME OVER")
    
    
    def main():
        word = choose_word(word_list)
        game_loop(word)
    
    if __name__ == "main":
        main()