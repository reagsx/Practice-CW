import string
def alphabet_position(text):
    text = text.replace(" ","").lower() #Remove Spaces and Make Lowercase
    for ch in string.punctuation:       #Remove Punctuation                                                                                              
        text = text.replace(ch, "") 
    output = []
    for i in text:                       #Find Position of Character in English Alphabet
            x = ord(i) - 96
            if x <= 26 and x > 0:
                output.append(x)
            else:                        #Returns nothing if it's outside of english alphabet range
                return ""

    return ' '.join(str(n) for n in output)
