import re, secrets, string, random, encode, sys

def findNames(file):
   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   names = re.findall(r'[A-Za-z_][A-Za-z0-9_]* =', code) # finds variable names preceding a =
   names += re.findall(r'[A-Za-z_][A-Za-z0-9_]*=', code) # finds variable names preceding a = w/o space
   names += re.findall(r'def [A-Za-z_][A-Za-z0-9_]*', code) # find function names
   file.close()

   for i in range(len(names)): # gets rid of the = in my list
      names[i] = names[i].rstrip(" =")
      if names[i].startswith("def "):
         names[i] = names[i].lstrip("def ")

   names = list(set(names)) # unique names

   for i in range(len(names) - 1, -1, -1):
      if names[i].startswith("__") and names[i].endswith("__"):
         del names[i]
   
   #print(names)
   return names

def replaceNames(file, output, version, key=None): # -v is vigenere, -m is random mapping, -s is random seed
   names = findNames(file)
   
   output = open(output, 'w')

   if version == "-m":
      # print("Random mapping mode.")
      map = {}
   elif version == "-v":
      # print("Vigenere mode.")
      if key is None or key == "None" or key == "":
         raise ValueError("Vigenère mode requires a key.")
      map = key
   elif version == "-s":
      # print("Random seed mode.")
      if key is None or key == "None" or key == "":
         raise ValueError("Seed mode requires a key.")
      map = {}
      output.write("key: " + key)
   else:
      raise ValueError("Please enter valid key.")

   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   file.close()

   for i in names:
      if version == "-m":
         length = random.randint(3, 10) # random length for the new variable name
         newName = ''.join(secrets.choice(string.ascii_letters) for _ in range(length)) # random string
         map[i] = newName
         #code = code.replace(i, newName)
         pattern = r'\b' + re.escape(i) + r'\b'
         code = re.sub(pattern, newName, code)
      if version == "-v":
         newName = encode.encode(i, key)
         pattern = r'\b' + re.escape(i) + r'\b'
         code = re.sub(pattern, newName, code)
         #code = code.replace(i, newName)
      if version == "-s":
         random.seed(i + key)
         length = random.randint(3, 10) # random length for the new variable name
         newName = ''.join(random.choice(string.ascii_letters) for _ in range(4))
         pattern = r'\b' + re.escape(i) + r'\b'
         code = re.sub(pattern, newName, code)
         # code = code.replace(i, newName)
         #print(newName)
         map[i] = length
   
   output.write(str(map))
   # print(code)
   #print(output)
   # print(map)
   
   return code


def findSpaces(code):
   # file = open(file, 'r')
   # code = file.read()

   symbols = ["=", "%", "<", ">", "≤", "≥", "=", ","]

   for i in symbols:
      code = code.replace(" " + i + " ", i)
      code = code.replace(" " + i, i)
      code = code.replace(i + " ", i)

   # print(code)
   # file.close()
   return code

def findNewLines(code):
   # file = open(file, 'r')
   # code = file.read()
   # file.close()
   code = re.sub(r'^\s*\n', '', code, flags=re.MULTILINE)
   #lines = re.findall(r'[A-Za-z_][A-Za-z0-9_]* =', code) # finds variable names preceding a =
   # print(code)
   return code

def getIndentUnit(s):
    if s.startswith('\t'):
        return '\t'
    elif s.startswith(' '):
        return ' ' * (len(s))
    else:
        return '    '
  
def makeDeadRet():
   length = random.randint(3, 10) # random length for the new variable name
   newName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
   deadRet = "if " + str(random.randint(3, 10)) + " == " + "0" + ":" + " return \"" + newName + "\"" + ";"
   return deadRet
   
def makeDeadif():
   length = random.randint(3, 10) # random length for the new variable name
   newName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
   deadIf = "if " + "(" + str(random.randint(3, 999)) + " + " + str(random.randint(1,999)) + ")" + "**2" " == " + "-1" + ":" + " " + "return \"" + newName + "\";"
   return deadIf

def deadCode(code):
#   file = open(file, 'r')
#   code = file.read()
#   file.close()

#  code = re.sub(r'(\s*)(?<!el)(if\s+.+?:)', lambda match: print(f'{match.group(0)}{match.group(1)}{getIndentUnit(match.group(1))}{makeDeadif()}'), code)
   code = re.sub(r'(\s*)(?<!el)(if\s+.+?:)', lambda match: f'{match.group(0)}{match.group(1)}{getIndentUnit(match.group(1))}{makeDeadif()}', code)
   code = re.sub(r'^(\s*)(return\b[^\n]*)$', lambda match: f'{match.group(0)}\n{match.group(1)}{makeDeadRet()}', code)

#   print(code)
   return code

def obfuscate(file, output, version, key=None):
   code = replaceNames(file, output, version, key)
   code = findSpaces(code)
   code = findNewLines(code)
   code = deadCode(code)

   print(code)
   return code


obfuscate(sys.argv[1], "output.txt", sys.argv[2], sys.argv[3])

#findNames("testingCodeFiles/crack.py")
#findSpaces("testingCodeFiles/crack.py")
#findNewLines("testingCodeFiles/crack.py")
#deadCode("testingCodeFiles/testInput.py")
#replaceNames("testingCodeFiles/crack.py", "output.txt", sys.argv[1], sys.argv[2])
# TODO current concerns: want to make sure that if i have a variable name reused in diff defs, it isn't an issue. i don't think it should be
# TODO test mapping file
# TODO change () variables too

