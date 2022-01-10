def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letterCount = dict()
    for let in phrase:
        val = letterCount.get(let,0)
        val = val + 1
        letterCount[let] = val

    return letterCount

        
