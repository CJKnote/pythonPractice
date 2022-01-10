def print_upper_words(word_list, must_start_with={}):
    """Takes a list of words and prints out each word but in uppercase,
    also takes a list of letters and only prints words that start with that letter

    
    for example: print_upper_words(['hello', 'hey', 'goodbye', 'bye'], must_start_with = {"h", "b"})
    
    will print:
        HELLO
        HEY
        BYE
    """
    for word in word_list:
        if word[0].lower() in must_start_with:
            print(word.upper())


print_upper_words(['hello', 'hey', 'goodbye', 'bye'], must_start_with = {"h", "b"})