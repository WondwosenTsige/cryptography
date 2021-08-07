import nltk

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

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
    return encrypt(encrypted_text, -shift_key)
    


def crack(encrypted_string):
    encrypted_words_list = encrypted_string.split()
    highest_word_count = 0
    most_probable_key = 0

    for x in range(1, 26):

        count = 0
        for word in encrypted_words_list:
            if decrypt(word, x) in word_list or decrypt(word, x) in name_list:  # name_list - line 90
                count += 1

        if count > highest_word_count:
            highest_word_count = count
            most_probable_key = x

    probability = highest_word_count / len(encrypted_words_list) * 100
    decrypted_word = decrypt(encrypted_string, most_probable_key)

    print(f"Decryption Probability: {probability}%")
    print(f"Most Probable Key: {most_probable_key}")
    return decrypted_word





if __name__ == "__main__":

    # input1 = "ABCD"
    # input2 = "abcd"
    # input3 = "ABab"
    # input4 = "AB ab AB cd dfadf  fasdf"

    # input5 = "Hello World. We did it."

    # result1 = encrypt(input5, 1453)
    # print(result1)

    # result2 = decrypt(result1, 1453)
    # print(result2)

    real_sentence = "It was the best of times, it was the worst of times."
    encrypted = encrypt(real_sentence, 18)

    result6 = crack(encrypted)
    print(result6)