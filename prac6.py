import random
import string

def encrypt(plain_text):
    key = generateKey(len(plain_text))
    cipher_text = ''
    for i in range(len(plain_text)):
        bitP = ord(plain_text[i]) - ord('a')
        bitC = ord(key[i]) - ord('a')
        cipher_text += chr(((bitP^bitC))%26+ord('a'))
    return key,cipher_text

def generateKey(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

messages = list(input("Enter messages with space : ").split(" "))
print(messages)
for msg in messages:
    key,cipher_text = encrypt(msg.lower())
    print("message : ",msg)
    print("key : ",key)
    print("Cipher : ",cipher_text)
    print("========================")