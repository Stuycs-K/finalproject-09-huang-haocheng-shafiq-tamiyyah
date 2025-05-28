import re

	# content = re.findall(r'[A-Za-z]+', content)
	# content = ''.join(content)


def findVarNames(file):
    file = open(file, 'r')
    code = file.read()
    varNames = re.findall(r'[A-Za-z]+ =', code)
    file.close()

    print(varNames)
    return varNames


findVarNames("code.txt")