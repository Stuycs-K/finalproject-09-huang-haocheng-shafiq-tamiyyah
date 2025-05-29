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


def replaceNames(file, output):
   names = findNames(file)


   map = {}


   file = open(file, 'r')  # opens file and reads it
   code = file.read()
   file.close()


   for i in names:
    #    length = random.randint(3, 10) # random length for the new variable name
    #    newName = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length)) # random string
       newName = encode.encode(i, "hao")
       code = code.replace(i, newName)
       map[i] = newName


   output = open(output, 'w')
   output.write(str(map))
  
   print(code)
   print(map)
   return code


replaceNames("testingCodeFiles/crack.py", "output.txt")
# TODO current concerns: want to make sure that if i have a variable name reused in diff defs, it isn't an issue. i don't think it should be
# TODO test mapping file

