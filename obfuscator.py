import re, secrets, string, random, encode

def findNames(file):
   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   names = re.findall(r'[A-Za-z]+ =', code) # finds variable names preceding a =
   names += re.findall(r'[A-Za-z]+=', code) # finds variable names preceding a = w/o space
   names += re.findall(r'def [A-Za-z]+', code) # find function names
   file.close()

   for i in range(len(names)): # gets rid of the = in my list
       names[i] = names[i].rstrip(" =")
       names[i] = names[i].lstrip("def ")

   names = list(set(names)) # unique names
   return names

def replaceNames(file, output, version, key=None): # -v is vigenere, -m is random mapping, -s is random seed
   names = findNames(file)

   if version == "-m":
      map = {}
   if version == "-v":
      if key is None:
         raise ValueError("Vigenère mode requires a key.")
      map = key

   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   file.close()

   for i in names:
      if version == "-m":
         length = random.randint(3, 10) # random length for the new variable name
         newName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
         map[i] = newName
         code = code.replace(i, newName)
      if version == "-v":
         newName = encode.encode(i, "hao")
         code = code.replace(i, newName)

   output = open(output, 'w')
   output.write(str(map))
  
   print(code)
   print(map)
   return code

def findSpaces(file):
   file = open(file, 'r')
   code = file.read()

replaceNames("testingCodeFiles/crack.py", "output.txt")
# TODO current concerns: want to make sure that if i have a variable name reused in diff defs, it isn't an issue. i don't think it should be
# TODO test mapping file