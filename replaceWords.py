replaceableWords = "I'm so proud of myself and the focus that I have. " # string of words that can be replaced

def replace_word(replaceableWords): 
    # define our exit list 
    # define our str of replaceable words
    # take an input. if input is in playerQuit, quit the program
    # if input is in changeableStr, call str.replace(old, new). print. rerun the program holding new str
    # else, print error. rerun the program
    
    playerQuit = ['quit', 'exit','f4']  # exit list
    print("type 'f4', 'quit', or 'exit' into the text box to stop") #   tell user leave instructions
    print("replace any word in the sentence: " + replaceableWords) # gives user replaceableWords
    word_to_replace = input("Enter the word to replace: ")  # user input for word in repaceableWords
    
    if word_to_replace in playerQuit: # Is the user input in our quit list?
        print("goodbye")
        return
    elif word_to_replace in replaceableWords: # is the user input in our phrase list?
        word_replacement = input("Enter the word replacement: ") # Get user input for for new word
        newPhrase = replaceableWords.replace(word_to_replace, word_replacement)
        replaceableWords = newPhrase
        print("Your new statement is: " + replaceableWords + "")
        replace_word(replaceableWords) # run it again with the new phrase to be replaced
    
replace_word(replaceableWords)