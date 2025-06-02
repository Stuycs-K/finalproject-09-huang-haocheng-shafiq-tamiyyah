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
   print(names)
   return names

def replaceNames(file, output, version, key=None): # -v is vigenere, -m is random mapping, -s is random seed
   names = findNames(file)

   if version == "-m":
      print("Random mapping mode.")
      map = {}
   elif version == "-v":
      print("Vigenere mode.")
      if key is None or key == "None" or key == "":
         raise ValueError("Vigenère mode requires a key.")
      map = key
   elif version == "-s":
      print("Random seed mode.")
      if key is None or key == "None" or key == "":
         raise ValueError("Seed mode requires a key.")
      map = {}
      map["key"] = key
   else:
      raise ValueError("Please enter valid key.")

   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   file.close()

   for i in names:
      if version == "-m":
         length = random.randint(3, 10) # random length for the new variable name
         newName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
         map[newName] = i
         code = code.replace(i, newName)
      if version == "-v":
         newName = encode.encode(i, key)
         code = code.replace(i, newName)
      if version == "-s":
         random.seed(i + key)
         length = random.randint(3, 10) # random length for the new variable name
         newName = ''.join(random.choice(string.ascii_letters) for _ in range(4))
         print(newName)
         map[i] = length

   output = open(output, 'w')
   output.write(str(map))
  
   print(code)
   print(map)
   return code

def findSpaces(file):
   file = open(file, 'r')
   code = file.read()

replaceNames("testingCodeFiles/crack.py", "output.txt", sys.argv[1], sys.argv[2])
# TODO current concerns: want to make sure that if i have a variable name reused in diff defs, it isn't an issue. i don't think it should be
# TODO test mapping file