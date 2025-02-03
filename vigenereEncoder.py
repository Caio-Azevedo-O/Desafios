def vigenereCifra(key, word):
    keyedAlpha = "oxesabcdfghijklmnpqrtuvwyz"
    abc = "abcdefghijklmnopqrstuvwxyz"
    lengthAlpha = len(abc)
    lengthKey = len(key)
    lengthWord = len(word)
    abcAux = keyedAlpha
    count = 0
    pointY = 0
    pointX = 0
    keyCipher = ""
    auxString = ""
    cipher = ""
    aux = ""
    vigenereTable = []
    vigenereTable.append(keyedAlpha)




    for i in range(lengthAlpha):
        auxString = keyedAlpha[i]
        abcAux = abcAux.replace(keyedAlpha[i], "")
        abcAux = abcAux+auxString
        abcAux = abcAux
        vigenereTable.append(abcAux)
        
        
    for i in range(lengthWord):
        aux = count
        if(lengthKey<=count):
            count = 0
        if(word[i]!=" "):
            keyCipher=keyCipher+key[count]
        count+=1
        if(word[i] == " "):
            keyCipher=keyCipher+" "
            count = aux




    for i in range(lengthWord):
        for j in range(lengthAlpha):
            if(word[i] == abc[j]):
                pointX = j
            if(keyCipher[i] == abc[j]):
                pointY = j
        aux = vigenereTable[pointX][pointY]
        if(word[i] == " "):
            cipher = cipher+" "
        if(word[i] != " "):
            cipher = cipher+aux




    return cipher


def vigenereDecifra(key, word):
    keyedAlpha = "oxesabcdfghijklmnpqrtuvwyz"
    abc = "abcdefghijklmnopqrstuvwxyz"
    lengthAlpha = len(abc)
    lengthKey = len(key)
    lengthWord = len(word)
    auxString = ""
    keyCipher = ""
    decipher = ""
    count = 0
    decipherX = 0
    arrayAux = []
    vigenereTable = []
    vigenereTable.append(keyedAlpha)
    abcAux = keyedAlpha
    
    for i in range(lengthAlpha):
        auxString = keyedAlpha[i]
        abcAux = abcAux.replace(keyedAlpha[i], "")
        abcAux = abcAux+auxString
        abcAux = abcAux
        vigenereTable.append(abcAux)
        
    for i in range(lengthWord):
        aux = count
        if(lengthKey<=count):
            count = 0
        if(word[i]!=" "):
            keyCipher=keyCipher+key[count]
        count+=1
        if(word[i] == " "):
            keyCipher=keyCipher+" "
            count = aux
            
    
    for i in range(lengthWord):
        for j in range(lengthAlpha):
            if(keyCipher[i] == abc[j]):
                arrayAux.append(j)
                
    for i in range(lengthWord):
        for j in range(lengthAlpha):
            if(word[i] == vigenereTable[j][arrayAux[i]]):
                decipherX = j
        decipher = decipher+abc[decipherX]
        
    return decipher
palavra = ""
chave = ""
palavra = input("Digite uma frase para encriptar: ")
chave = input("Digite a palavra chave que será usada para encriptar: ")
print(vigenereCifra(str.lower(chave), str.lower(palavra)))


palavraDecifra = input("Decifra: ")
chaveDecifra = input("Chave: ")
print(vigenereDecifra(str.lower(chaveDecifra), str.lower(palavraDecifra)))
