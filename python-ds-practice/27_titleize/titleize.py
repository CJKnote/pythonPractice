def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.lower()
    phraseWords = phrase.split(" ")

    title = ""
    for word in phraseWords:
        title += word.capitalize() + " "

    #remove space at end
    return title.strip()

