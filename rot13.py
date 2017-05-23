import string
from codecs import encode as _dont_use_this_

def rot13(message):
    t = ""
    for i in message:
        if i.isalpha():
            if ord(i) > 65 and ord(i) < 91:
                if ord(i) < 78:
                    t += chr(ord(i) + 13)
                else:
                    t += chr(ord(i) - 13)
            else:
                if ord(i) < 110:
                    t += chr(ord(i) + 13)
                else:
                    t += chr(ord(i) - 13)
        else:
            t += i
    return t