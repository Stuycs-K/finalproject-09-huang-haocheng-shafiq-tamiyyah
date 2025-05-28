import re

	# content = re.findall(r'[A-Za-z]+', content)
	# content = ''.join(content)


def findVarNames(file):
    file = open(file, 'r')  # opens file and reads it
    code = file.read()
    varNames = re.findall(r'[A-Za-z]+ =', code) # finds everything preceding a =
    file.close()

    for i in range(len(varNames)): # gets rid of the = in my list
        varNames[i] = varNames[i].rstrip(" =")

    print(varNames)
    return varNames


findVarNames("code.txt")