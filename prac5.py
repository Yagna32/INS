import numpy as np
import math
def encrypt_with_startswith0(phrase, alphaZero):
    def echoResult1(label, adder, phrase):
        result = label
        for i in range(0, len(phrase), 2):
            result += chr(phrase[i] + (64 + adder)) + chr(phrase[i + 1] + (64 + adder))
            if i + 2 < len(phrase):
                result += "-"
        print(result)

    def echoResult(label, adder, phrase):
        print(label)
        for i in range(0, len(phrase), 2):
            print(f"{chr((phrase[i] % 26) + 64 + adder)} ({phrase[i]}), {chr((phrase[i + 1] % 26) + 64 + adder)} ({phrase[i + 1]})")

    def encrypt(phrase, alphaZero):
        adder = 1 if alphaZero else 0
        phrase = ''.join(filter(str.isalpha, phrase)).upper()
        if len(phrase) % 2 == 1:
            phrase += "X"
        print("Phrase",phrase,ord('a'))
        key = input("Enter key: ").replace(" ", "")
        keyMatrix = np.zeros((2, 2), dtype=int)
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i, j] = (ord(key[k]) - ord('a'))
                k += 1
        
        print("Plain Text Values:")
        for i in range(0, len(phrase), 2):
            print(f"{phrase[i]} ({(ord(phrase[i]) - 65) % 26})", f"{phrase[i + 1]} ({(ord(phrase[i + 1]) - 65) % 26})")

        
        phraseToNum = [(ord(c) - (64 + adder)) for c in phrase]
        print(phraseToNum)
        phraseEncoded = []
        for i in range(0, len(phraseToNum), 2):
            x = (keyMatrix[0, 0] * phraseToNum[i] + keyMatrix[0, 1] * phraseToNum[i + 1]) % 26
            y = (keyMatrix[1, 0] * phraseToNum[i] + keyMatrix[1, 1] * phraseToNum[i + 1]) % 26

            phraseEncoded.extend([x, y])
        print(phraseEncoded)
        print("--------------------------------------")
        echoResult("encrypted pair: ", adder, phraseEncoded)
        print("--------------------------------------")
        echoResult1("encrypted text: ", adder, phraseEncoded)
    
    encrypt(phrase, alphaZero)
    

def encrypt_with_startswith1(phrase, alphaZero):
    def echoResult1(label, adder, phrase):
        result = label
        for i in range(0, len(phrase), 2):
            result += chr(phrase[i] + (63 + adder)) + chr(phrase[i + 1] + (63 + adder))
            if i + 2 < len(phrase):
                result += "-"
        print(result)
    
    def echoResult(label, adder, phrase):
        print(label)
        for i in range(0, len(phrase), 2):
            char1 = chr(((phrase[i] - 1) % 26) + 64 + adder) if phrase[i] != 0 else 'Z'
            char2 = chr(((phrase[i + 1] - 1) % 26) + 64 + adder) if phrase[i + 1] != 0 else 'Z'
            index1 = 26 if phrase[i] == 0 else phrase[i]
            index2 = 26 if phrase[i + 1] == 0 else phrase[i + 1]
            print(f"{char1} ({index1}), {char2} ({index2})")


    def encrypt(phrase, alphaZero):
        adder = 1 if alphaZero else 0
        phrase = ''.join(filter(str.isalpha, phrase)).upper()
        if len(phrase) % 2 == 1:
            phrase += "X"
        
        key = input("Enter key: ").replace(" ", "").upper()
        keyMatrix = np.zeros((2, 2), dtype=int)
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i, j] = (ord(key[k]) - 65)+1  # Convert A=1 indexing
                k += 1
        
        print("Plain Text Values:")
        for i in range(0, len(phrase), 2):
            print(f"{phrase[i]} ({(ord(phrase[i]) - 64) % 26 })", f"{phrase[i + 1]} ({(ord(phrase[i + 1]) - 64) % 26 })")

        phraseToNum = [(ord(c) - (63 + adder)) for c in phrase]
        phraseEncoded = []
        for i in range(0, len(phraseToNum), 2):
            # print("phraseToNum[i]")
            # print(phraseToNum[i])
            # print("phraseToNum[i+1]")
            # print(phraseToNum[i+1])
            x = (keyMatrix[0, 0] * phraseToNum[i] + keyMatrix[0, 1] * phraseToNum[i + 1]) % 26
            # print("x")
            if(x==0): x=26
            # print(x)
            y = (keyMatrix[1, 0] * phraseToNum[i] + keyMatrix[1, 1] * phraseToNum[i + 1]) % 26
            # print("y")
            if(y==0): y=26
            # print(y)

            phraseEncoded.extend([x, y])
       
        print("-----------------------------------------")
        echoResult("Encrypted pair: ", adder, phraseEncoded)
        print("-----------------------------------------")
        echoResult1("Encrypted text: ", adder, phraseEncoded)


    encrypt(phrase, alphaZero)



def echoResult_decrypt(label, adder, phrase):
    print("-----------------------------------------")
    print(label)
    for i in range(0, len(phrase), 2):
        char1 = chr(((phrase[i] - 1) % 26) + 64 + adder) if phrase[i] != 0 else 'Z'
        char2 = chr(((phrase[i + 1] - 1) % 26) + 64 + adder) if phrase[i + 1] != 0 else 'Z'
        index1 = 26 if phrase[i] == 0 else phrase[i]
        index2 = 26 if phrase[i + 1] == 0 else phrase[i + 1]
        print(f"{char1} ({index1})", f"{char2} ({index2})")

def echoResult1_decrypt(label, adder, phrase):
    result = label
    for i in range(0, len(phrase), 2):
        result += chr(phrase[i] + (63 + adder)) + chr(phrase[i + 1] + (63 + adder))
        if i + 2 < len(phrase):
            result += "-"
    print(result)


def decrypt(phrase, alphaZero):
    adder = 1 if alphaZero else 0
    phrase = ''.join(filter(str.isalpha, phrase)).upper()
    if len(phrase) % 2 == 1:
        phrase += "X"
    
    key = input("Enter key: ").replace(" ", "").upper()
    # key = "dacb"
    keyMatrix = np.zeros((2, 2), dtype=int)
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i, j] = (ord(key[k]) - 65) + 1  # Convert A=1 indexing
            k += 1
    

    print("Plain Text Values:")
    for i in range(0, len(phrase), 2):
        char1_index = (ord(phrase[i]) - 65) % 26 + 1  # Convert to index starting from 1
        char2_index = (ord(phrase[i + 1]) - 65) % 26 + 1  # Convert to index starting from 1
        print(f"{phrase[i]} ({char1_index})", f"{phrase[i + 1]} ({char2_index})")
    
    det = keyMatrix[0, 0] * keyMatrix[1, 1] - keyMatrix[1, 0] * keyMatrix[0, 1]
    mod_det = det % 26
    if not (math.gcd(mod_det,26)==1):
        print("not invertible")
        return
    kInverse = 1
    while (mod_det * kInverse) % 26 != 1 and kInverse<26:
        kInverse += 1
    if kInverse==26:
        print("Not invertible")
        return
    kInverseMatrix = np.array([[keyMatrix[1, 1], -keyMatrix[0, 1]], [-keyMatrix[1, 0], keyMatrix[0, 0]]])
    kInverseMatrix = (kInverseMatrix * kInverse) % 26
    
    print("-----------------------------------------")
    print("Inverse Key Matrix:")
    print(kInverseMatrix)

    phraseToNum = [(ord(c) - (63 + adder)) for c in phrase]
    # print(phraseToNum)
    phraseDecoded = []
    for i in range(0, len(phraseToNum), 2):
        # print("phraseToNum[i]")
        # print(phraseToNum[i])
        # print("phraseToNum[i+1]")
        # print(phraseToNum[i+1])
        
        x = (kInverseMatrix[0, 0] * phraseToNum[i] + kInverseMatrix[0, 1] * phraseToNum[i + 1]) % 26
        if(x==0): x=26
        # print("x")
        # print(x)
        y = (kInverseMatrix[1, 0] * phraseToNum[i] + kInverseMatrix[1, 1] * phraseToNum[i + 1]) % 26
        if(y==0): y=26
        # print("y")
        # print(y)
        phraseDecoded.extend([x, y])


    print("-----------------------------------------")
    echoResult_decrypt("Decrypted pair: ", adder, phraseDecoded)
    print("--------------------------------------")
    echoResult1_decrypt("Decrypted text: ", adder, phraseDecoded)
    
    

print("Hill Cipher Implementation (2x2)")
print("-------------------------")
print("1. Encrypt text (A=0,B=1,...Z=25)")
print("2. Encrypt text (A=1,B=2,...Z=26)")
print("3. Decrypt text (A=1,B=2,...Z=26)")
print()

opt = input("Select your choice: ")
phrase = input("Enter plaintext: ")

if opt == "1":
    encrypt_with_startswith0(phrase, True)
elif opt == "2":
    encrypt_with_startswith1(phrase,True)    
elif opt == "3":
    decrypt(phrase,True)
else:
    print("Invalid choice")

