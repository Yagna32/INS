import string

matrix = []
alphabet = list(string.ascii_lowercase)

for i in range(26):
    row = alphabet[i:] + alphabet[:i]
    matrix.append(row)

plain_text = input("Enter plain text : ").lower()
key = input("Enter key : ")
while not len(key) == len(plain_text):
    i = len(plain_text) - len(key)
    key += key[:i]

print("revised key : ",key)
cipher = ""
for i in range(len(plain_text)):
    indexP = ord(plain_text[i])-ord('a')
    indexC = ord(key[i])-ord('a')
    cipher += matrix[indexP][indexC]

print("Cipher : ",cipher)