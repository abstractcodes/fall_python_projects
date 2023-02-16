# import statements written.
from distutils import extension
from webbrowser import get


def main():
    """ Main function to get the right filename
    and separate cipher key from set of words and then decrypt it
    and print it"""
    get_file_name = getInputFile()
    # opening the file for decryption.
    continue_running = True
    # handling whether the file exists in the database or not.
    while continue_running:
        try:
            fileopen = open(get_file_name,"r")
        except FileNotFoundError:
            print("File not found please input the file again")
            get_file_name = getInputFile()
        else:
            continue_running = False
    # separating words and cipher key.
    make_list = list(fileopen)
    cipher_key = int(make_list[0].strip())
    encrypted_message = make_list[1]
    # decrypting the message.
    decrypted_message = decrypt(cipher_key,encrypted_message)
    print(decrypted_message)
    # asking for encryption of message.
    ask_question = (input("Do you like to test encryption of a message. Input yes or no:" )).lower()
    if ask_question == "yes":
        encrypt()
    else:
        print("Thak you your file containg the message with the cipher key is decrypted.")
    fileopen.close()

def getInputFile():
    """this function takes no arguments and is used to check
    whether the file is of the correct extension .txt or not and 
    then return the file if it is of .txt extension"""
    input_filename = input("Enter the input filename:")
    # right file not entered.
    while "." not in input_filename:
        input_filename = input("Enter the input filename:")
    # index function is used to get the index of the period.
    get_period_index = input_filename.index(".")
    # getting the extension.
    extension = input_filename[get_period_index+1:len(input_filename)]
    # repetedly asking for the right file with the right extension.
    while extension != "txt":
        print("Invalid filename extension. Please re-enter the input filename:",input_filename)
        input_filename = input("Enter the input filename:")
        get_period_index = input_filename.index(".")
        extension = input_filename[get_period_index+1:len(input_filename)]
    return input_filename

def decrypt(key,message):
    """this function with two arguments which is the key and the message to be derypted 
    is uded to decrypt the message and then return the decrypted message."""
    list_of_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #list_of_alphabets = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
    decrypt = ""
    for element in message:
        if element != " ":
            # lower function is used to conver all letters to lowercase.
            index_of_element = list_of_alphabets.index(element.lower())
            increment = abs(index_of_element - key)
            # concept of wrapping is used.
            decrypt = decrypt + list_of_alphabets[increment%len(list_of_alphabets)]
        else:
            decrypt = decrypt + " "
    return decrypt

def encrypt(message,key):
    """ this function takes no arguments and is used to
    encrypt a message with a specific cipher key."""
    '''
    get_file = getInputFile()
    # opening the file to write the encrypted message in.
    file_write = open(get_file,"w")
    # asking for message which only contains letters and whitespaces.
    message = input("Please enter a message which contains only letters and spaces: ")
    remove_spaces = message.split()
    join_elements = "".join(remove_spaces)
    while join_elements.isalpha() == False:
        message = input("Please enter a message which contains only letters and spaces: ")
        remove_spaces = message.split()
        join_elements = "".join(remove_spaces)
        # asking for cipher key which only contains integer number.
    enter_cipher_key = input("Enter the cipher key: ")
    while enter_cipher_key.isdigit() == False:
        enter_cipher_key = input("Enter cipher key which is an integer number: ")
    # converting to integer.
    enter_cipher_key = int(enter_cipher_key)'''
    # process of enryption.
    print(message)
    list_of_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encrypt = ""
    for element in message:
        if element != " ":
            index_of_element = list_of_alphabets.index(element.lower())
            increment = index_of_element + key
            encrypt = encrypt + list_of_alphabets[increment%len(list_of_alphabets)]
        else:
            encrypt = encrypt + " "
    '''
    # writing into the file.
    file_write.write(str(enter_cipher_key)+"\n")
    file_write.write(encrypt.upper())
    file_write.close()'''

def main2():
    input_text = input("Please enter a text for encryption or decryption: ")
    input_key = int(input("Enter a key for encryption or decryption: "))
    print(decrypt(input_text.upper(),input_key))


# main function is called.     
main2()