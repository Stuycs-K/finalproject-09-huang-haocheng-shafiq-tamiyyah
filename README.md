[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Code Obfuscation and Deobfuscation
 
### neverlate

Tamiyyah Shafiq and Haocheng Huang

### Project Description:

Explain what is this project. (CHANGE THIS!!!!!)
  
### Instructions:

1. Have the required program files: the `makefile`, `encode.py`, and `obfuscator.py`, as well as a python program that you want to obfuscate in the same directory.
2. Use `make run` to run the program, but make sure to include the following arguments:
	- to pick a obfuscation version, use one of the following flags 
		- `-m` for random mapping identifier renaming
		- `-v` for vigenere identifier renaming
		- `-s` for seeded random identifier renaming
	- the key used for vigenere or the seed used for seeded random
   For example, to run the code with make, it would be formatted like this:
	```make run ARGS="-v randomkey"```
### Resources/ References:
* https://github.com/ericyoc/obfuscation_techniques_poc/blob/main/README.md
* https://www.techtarget.com/searchsecurity/definition/obfuscation
* https://obfuscator.io
* https://medium.com/@hendurhance/how-obfuscation-works-in-software-development-7f52edfff520
