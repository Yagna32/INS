# # --------------------------------Encryption 

# Ptext=input('Enter a plain text : ')
# key=int(input('Enter a key : '))

# print(f'\t->Plain text: {Ptext}')
# encryptedString=''

# print('\n->Encryption:')
# for i in Ptext:
#     if i == ' ':
#         encryptedString+=' '
#     elif i>='a' and i<='z':
#         encryptedString+=chr(((ord(i)+key-97)%26)+97)
#     else:
#         encryptedString+=chr(((ord(i)+key-65)%26)+65)

# print(f'\t-> Encrypted text is: {encryptedString}')

# cipherText=input('Enter a cipher text: ')
# print('cipher text:',cipherText)
# for key in range(1,26):
#     originalText=''
#     for i in cipherText:
#         if i == ' ':
#             originalText+=' '
#         elif i>='a' and i<='z':
#             originalText+=chr(((ord(i)-key-97)%26)+97)
#         else:
#             originalText+=chr(((ord(i)-key-65)%26)+65)
#     print(f'Using Key: {key} we got Text: {originalText}')

# ------------------------------mono alpha 
def key_validation(key):
    return len(key) == 26 and len(set(key)) == 26

def enciphering(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            index = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')
            cipher_text += key[index].lower() if char.islower() else key[index].upper()
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    deciphering_text = ""
    for char in cipher_text:
        if char.isalpha():
            index = key.lower().index(char) if char.islower() else key.index(char)
            deciphering_text += chr(index + ord('a')) if char.islower() else chr(index + ord('A'))
        else:
            deciphering_text += char
    return deciphering_text

def main():
    secret_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    plain_text = input("Enter the plain text to encrypt: ")
    cipher_text = enciphering(plain_text, secret_key)
    print("Encrypted text:", cipher_text)

    cipher_text = input("Enter the cipher text to decipher : ")
    while True:
        decryption_key = input("Enter the key : ")
        if not key_validation(decryption_key):
            print("Invalid key! Try Again : ")
        else:
            break

    decrypted_text = decrypt(cipher_text, decryption_key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
