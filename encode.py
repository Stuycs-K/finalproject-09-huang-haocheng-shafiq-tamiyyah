import re
import sys

def encode(text, key):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	# text = open(textFile, 'r')
	# content = text.read().upper()
	# content = re.findall(r'[A-Za-z]+', content)
	# content = ''.join(content)

	# openKey = open(keyFile, 'r')
	# ky = openKey.read().upper()
	# key = ky.strip()

	# text.close()
	# openKey.close()

	key = key.upper()

	result = []

	for i in range(len(text)):
		result.append([])
		# print(key[i%len(key)])
		# print(i)
		# print(len(key))
		# print(key)
		shift = alphabet.index(key[i % len(key)])
		encoded = rotate(text[i], shift)
		result[i] = encoded

	return ''.join(result)

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

# print(encode("cat", "haha"))

# print(encode(sys.argv[1], sys.argv[2]))
