import re, secrets, string, random

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
        length = random.randint(3, 10) # random length for the new variable name
        newVarName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
        code = code.replace(i, newVarName)
    
    print(code)
    return code

replaceVarNames("testingCodeFiles/crack.py")

# current concerns: want to make sure that if i have a variable name reused in diff defs, it isn't an issue. i don't think it should be