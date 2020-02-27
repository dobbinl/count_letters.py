
import string
alphabet = string.ascii_uppercase
def count_letters(s):
    """
        Imported string built in order to check
        the passed in string for uppercase lettering.
        :program makes string uppercase prior to for loop.
        :conducts and increment count of characters.
        """
    d = dict()
    s = s.upper()

    for c in s:
        if c in alphabet:
            # increment count in the dict
            if c not in d:
                d[c] = 1
            else: # c is in the dict
                d[c] +=1
    return d

