import string
alphabets = string.ascii_lowercase

def alphabet_position(text):
    #creating dictionary ;
    text = text.lower()
    dictionary = {}
    new_string = ''
    x=1
    for alphabet in alphabets:
        dictionary[alphabet] = str(x)
        x += 1
    for letter in text:
        if letter in alphabets:
            new_string = new_string + dictionary[letter] + ' ' 
    return new_string.strip(' ')


