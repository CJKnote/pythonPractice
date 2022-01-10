def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    #should ignore capitiliation and spaces:
    lower_phrase = phrase.lower()
    lower_NS_phrase = lower_phrase.replace(" ", "")

    count = -1
    for let in lower_NS_phrase:
        if let != lower_NS_phrase[count]:
            return False
        else:
            count = count - 1
    return True
    
