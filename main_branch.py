def decode(password):
    Dstring = ''
    for char in password:
        char1 = int(char) - 3
        Dstring += str(char1)
    return Dstring
