import nltk

def encrypt(plain_text, shift_key):
    
    string = ""

    for char in plain_text:
        converted = ord(char)

        if converted >= 97 and converted <= 122:
            added = converted + shift_key
            if added > 122 or added < 97:
                difference = added - 123
                modulo = difference % 26
                string += chr(97 + modulo)
            else:
                string += chr(added)

        elif converted >= 65 and converted <= 90:
            added = converted + shift_key
            if added > 90 or added < 65:
                difference = added - 91
                modulo = difference % 26
                string += chr(65 + modulo)
            else:
                string += chr(added)

        else:
            string += char

    return string

def decrypt(encrypted_text, shift_key):
    return decrypt(encrypted_text, -shift_key)
    






if __name__ == "__main__":

    input1 = "ABCD"
    input2 = "abcd"
    input3 = "ABab"
    input4 = "AB ab AB cd dfadf  fasdf"

    input5 = "Hello World. We did it."

    result1 = encrypt(input5, 1453)
    print(result1)

    result2 = decrypt(result1, 1453)
    print(result2)