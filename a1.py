from math import log2

def encrypt(text, key):
    """
    encrypt(text, key) - takes a ciphertext (encrypted text) and a short key,
    and deciphers it using vigenere's cipher
    text - Some text as a str. All characters must be in ALPHABET
    key - Some text as a str. All characters must be in ALPHABET
    return - encrypted text
    """
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    for position in range(len(text)):
        text_character = ALPHABET.index(text[position])
        if len(key) == 1:
            key_character = ALPHABET.index(key)
        else:
            key_character = ALPHABET.index(key[position % len(key)])
        encrypted_char = (text_character + key_character) % len(ALPHABET)
        encrypted += ALPHABET[encrypted_char]
    return encrypted

def decrypt(text , key):
    """
    encrypt(text, key) - takes a text and decrypts it using vigenere's cipher.
    text - Some text as a str. All characters must be in ALPHABET
    key - Some text as a str. All characters must be in ALPHABET
    return - decrypted text
    """
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Reverse_ALPHABET = ALPHABET[::-1]
    decrypted = ""
    for position in range(len(text)):
        text_character = Reverse_ALPHABET.index(text[position])
        if len(key) == 1:
            key_character = ALPHABET.index(key)
        else:
            key_character = ALPHABET.index(key[position % len(key)])
        decrypted_char = ((text_character + key_character)) % len(Reverse_ALPHABET)
        decrypted += Reverse_ALPHABET[decrypted_char]
    return decrypted

def get_frequencies(text):
    """
    get_frequiencies(text) - takes a text and finds the frequencies of each unique character 
    in the text and stores it as a dictionary.
    text - Some text as a str.
    return - dictionary storing freqencies.
    """
    frequency_dictionary = {}
    for element in text:
        if element not in frequency_dictionary:
            frequency_dictionary[element] = (text.count(element)) / len(text)
    return frequency_dictionary

def cross_entropy(freq1,freq2):
    """
    cross_entropy(fre1,freq1) - there are two dictionaries and it compares the frequencies of two dictionaries.
    freq1 - some dictionary containing frequencies of each character.
    freq2 - another dictionary containing frequencies of each character.
    return - a float value which is the comparison of frequencies.
    """
    total = 0.0
    # stores the unique characters in a list.
    same_characters = list(freq1.keys())
    for elements in freq2.keys():
        if elements not in same_characters:
            same_characters.append(elements)
    # stores minimum frequencies of each dictionary.
    min_freq1 = min(list(freq1.values()))
    min_freq2 = min(list(freq2.values()))
    # compares and stores frequiencies and subtracts from total only once.
    for items in same_characters:
        if items in freq1 and items not in freq2:
            frequency_1 = freq1[items]
            frequency_2 = min_freq2
        elif items in freq2 and items not in freq1:
            frequency_1 = min_freq1
            frequency_2 = freq2[items]
        else:
            frequency_1 = freq1[items]
            frequency_2 = freq2[items]
        total -= frequency_1*log2(frequency_2)

    return (abs(total))

def guess_key(encrypted):
    """
    gues_key(encrypted)) - takes a ciphertext (encrypted text) and guesses the key.
    encrypted - Some text as a str. All characters must be in ALPHABET.
    return - key of length three.
    """
    ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # reading the file
    with open("frank.txt","r") as fileopen:
        file_open = fileopen.read()    
        english_frequencies = get_frequencies(file_open)
        fileopen.close()
    # making isolated text
    isolated_text_1 = encrypted[0::3] 
    isolated_list_1 = []
    isolated_text_2 = encrypted[1+3::3]
    isolated_list_2 = []
    isolated_text_3 = encrypted[2::3]
    isolated_list_3 = []

    # comparing frequencies
    for elements in ALPHABET:
        isolated_list_1.append(cross_entropy(english_frequencies, get_frequencies(decrypt(isolated_text_1 , elements))))
        isolated_list_2.append(cross_entropy(english_frequencies, get_frequencies(decrypt(isolated_text_2 , elements))))
        isolated_list_3.append(cross_entropy(english_frequencies, get_frequencies(decrypt(isolated_text_3 , elements))))
    
    key = ALPHABET[isolated_list_1.index(min(isolated_list_1))] + ALPHABET[isolated_list_2.index(min(isolated_list_2))] + ALPHABET[isolated_list_3.index(min(isolated_list_3))]

    return key

def crack(encrypted_text):
    """
    crack(encrypted_text) - takes a ciphertext (encrypted text) and decrypts it using decrypt function.
    encrypted_text - Some text as a str.
    return - decrypted text.
    """
    decrypted_text = decrypt(encrypted_text,guess_key(encrypted_text))
    return decrypted_text


def main():
    """
    controls the main functionality of the program.
    main() - it opens the encrypted file and cracks it using the guess key method and prints it.
    return - none.
    """
    with open("frank_encrypted.txt","r") as filename:
        encrypt_text = filename.read()
        filename.close()
    decrypt = crack(encrypt_text)
    print(decrypt)

# According to the software quality requirements main is called in this way.
if __name__=="__main__":
    main()