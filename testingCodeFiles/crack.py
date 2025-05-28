import sys
import math
import re

def getKey(text):
    file = open(text, 'r')
    content = file.read()
    extra = ""

    dist = 100
    key = ""
    finalI = 0
    for i in range(1, 13):
        brokenUp = breakApart(text, i)
        decoded = caesar(brokenUp)
        decoded = merge(decoded)
        dista = distance(english_frequency, freq(decoded))
        #print(i)
        #print(dista)
        if dista == dist:
            extra = ""
        if dista < dist:
            dist = dista
            key = decoded
            finalI = i
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = content
    plain = key
    bigKey = ""

    for i in range(len(plain) - 1):
        #print(alphabet.index(plain[i]))
        rotated = rotate(alphabet, alphabet.index(plain[i]))
        #print(rotated)
        #print(cipher[i])
        var = rotated.index(cipher[i])
        bigKey += alphabet[var]

    return bigKey[0:finalI]

def breakApart(text, key):
    file = open(text, 'r')
    content = file.read()
    
    wordList = []
    
    for i in range(key):
        wordList.append([])
   
    for i in range(len(content)):
        wordList[i%key].append(content[i])
        
    result = []

    for i in wordList:
        result.append(''.join(i))

    return result

def freq(string):
    retArray = [0]*26    
    content = string.upper()
    content = re.findall(r'[A-Za-z]+', content)
    text = "".join(content)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        count = len(re.findall(letter, text))
        retArray[alphabet.index(letter)] = count/len(text)
    return retArray

def freqF(filename):
    retArray = [0]*26    
    file = open(filename, 'r')
    content = file.read().upper()
    content = re.findall(r'[A-Za-z]+', content)
    text = "".join(content)
    file.close()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        count = len(re.findall(letter, text))
        retArray[alphabet.index(letter)] = count/len(text)
    return retArray

english_frequency = freqF("alice_in_wonderland.txt")
message_frequency = freqF(sys.argv[1])

def distance(arrayOne, arrayTwo):
    distance = 0
    length = len(arrayOne)
    for i in range(length):
        distance += (arrayOne[i] - arrayTwo[i])**2
    
    return math.sqrt(distance)

def rotate(content, shift):
    alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetL = "abcdefghijklmnopqrstuvwxyz"

    result = []
    
    for i in content:
        if i.isalpha():
            if i.isupper():
                index = alphabetU.index(i)
                newIndex = (index + shift) % 26
                newLet = alphabetU[newIndex]
                result.append(newLet)
            else:
                index = alphabetL.index(i)
                newIndex = (index + shift) % 26
                newLet = alphabetL[newIndex]
                result.append(newLet)
        else:
            result.append(i)
    return ''.join(result)

def findRot(text):
    minDistance = distance(english_frequency, message_frequency)
    shift = 0
    
    for i in range(27):
        message = rotate(text, i)
        messFreq = freq(message)
        dist = distance(english_frequency, messFreq)
        if dist < minDistance:
            minDistance = dist
            shift = i
    
    return shift

def reverse(text):
    alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetL = "abcdefghijklmnopqrstuvwxyz"

    result = []
    
    for i in text:
        if i.isalpha():
            if i.isupper():
                index = alphabetU.index(i)
                newLet = alphabetU[25 - index]
                result.append(newLet)
            if i.islower():
                index = alphabetL.index(i)
                newLet = alphabetL[25 - index]
                result.append(newLet)
        else:
            result.append(i)
    return ''.join(result)

def decode(text):    
    rotNum = findRot(text)
    messageOg = rotate(text, rotNum)
    distanceOg = distance(english_frequency, freq(messageOg))
    
    reversem = reverse(text)
    rotNumRev = findRot(reversem)
    messageRev = rotate(reversem, rotNumRev)
    distanceRev = distance(english_frequency, freq(messageRev))
    
    if distanceOg < distanceRev:
        return messageOg
    else:
        return messageRev

def caesar(array):
    result = []
    for i in array:
        result.append(decode(i))
    
    return result
        
def merge(array):
    result = []
    for i in range(len(array[0])):
        for j in array:
            if i < len(j):
                result.append(j[i])
    
    return ''.join(result)
                
#print(getKey(sys.argv[1]))

def crack(cipher):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    text = open(cipher, 'r')
    content = text.read().strip()
    text.close()

    result = []

    key = getKey(cipher)

    for i in range(len(content)):
        result.append([])
        shift = alphabet.index(key[i % len(key)])
        alphaShift = rotate(alphabet, shift)
        var = alphaShift.index(content[i])
        result[i] = alphabet[var]

    return ''.join(result)

print(crack(sys.argv[1]))