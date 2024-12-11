letter_alphabet='abcdefghijklmnopqrstuvwxyz'
number_letters= len(letter_alphabet)

def encrypt(plain_text, key): #C= P+key(integer value) mod 26 #C= Cipher Text #P=Plain Text
    cipher_text = ''
    for letter in plain_text:
        letter = letter.lower()
        if not letter == ' ':
            index= letter_alphabet.find(letter)
            if index == -1:
                cipher_text += letter
            else:
                new_index = index + key
                if new_index >= number_letters: 
                    new_index -= number_letters
                cipher_text+=letter_alphabet[new_index]
    return cipher_text

def decrypt(cipher_text, key): #P= C-key(integer value) mod 26 #C= Cipher Text #P=Plain Text
    plain_text = ''
    for letter in cipher_text:
        letter=letter.lower()
        if not letter == ' ':
            index= letter_alphabet.find(letter)
            if index == -1:
                plain_text += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += number_letters
                plain_text+=letter_alphabet[new_index]
    return plain_text
                

print()
print('***** Welcome to Caeser Cipher Encryption & Decryption Technique *****')
print('                 *** Build By Mohamed Yusuf Mujawar ***               ')
print()
print('Do you want to use encrypt or decrypt technique')
user_input=input('Encrypt / Decrypt: ').lower()
print()

if user_input == 'encrypt':
    print('Encryption Technique Selected')
    print()
    key=int(input('Enter the key(1 through 26):' ))
    print()
    text=input('Enter the message from user:')
    print()
    cipher_text=encrypt(text, key)
    print()
    print(f'CIPHER TEXT MESSAGE: {cipher_text}')
    print()
    
elif user_input == 'decrypt' :
    print('Decryption Technique Selected')
    print()
    key=int(input('Enter the key 1 through 26:'))
    print()
    text=input('Enter the message from user:')
    print()
    plain_text=decrypt(text, key)
    print()
    print(f'PLAIN TEXT MESSAGE: {plain_text}')
    print()

