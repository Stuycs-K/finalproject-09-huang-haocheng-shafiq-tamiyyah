import re

	# content = re.findall(r'[A-Za-z]+', content)
	# content = ''.join(content)


def findVarNames(file):
    file = open(file, 'r')  # opens file and reads it
    code = file.read()
    varNames = re.findall(r'[A-Za-z]+ =', code) # finds everything preceding a =
    varNames += re.findall(r'[A-Za-z]+=', code) # finds everything preceding a = w/o space
    file.close()

    for i in range(len(varNames)): # gets rid of the = in my list
        varNames[i] = varNames[i].rstrip(" =")

    return varNames

def replaceVarNames(file):
    varNames = findVarNames(file)

    file = open(file, 'r')  # opens file and reads it
    code = file.read()
    file.close()

    for i in varNames:
        code = code.replace(i, "AAAAH")
    
    print(code)
    return code



replaceVarNames("testingCodeFiles/code.txt")

