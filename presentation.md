



## Code Obfuscation

### who:

Developers of:
- Commertial Software - to protect intellectual property
- Malware - to conceal malicious behavior and avoid detection
- Games - to prevent reverse engineering
- Cybersecurity tools - also to prevent reverse engineering and protect sensitive logic

### what:

**Code obfuscation** - ‘transforming’ of code into a form that is difficult for humans to read/understand while preserving the functionality


![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdDTJ3Wc3VIwyvEpiFxptSPEuqZ5rWeROm1la_RMItCoLZXTMST7JbaS00X4oQruyGu_TwB-KTwzAdFE5l0olOlwiqfXaXsjV4YdUj8546NdM8jTK4_IohSBruYc2thTh187pCN3Q?key=dhwPmVRPu3kT5ODhTTZ5fg)

### where:
Not every language is easy to obfuscate
Some languages, like Java, C, and C++, are easy to obfuscate because they compile to bytecode or machine code, which gives more room for obfuscation techniques since the source code is less accessible

Other languages like Python is hard to obfuscate because it prioritizes being readable and using common obfuscation techniques results in code that can still be easily interpreted
### when and why:
- before releasing software or scripts to the public
- during malware creation to hide malicious intent
- in anti-piracy mechanisms to prevent tampering or bypassing
- hide proprietary code from competitors
### how:

- **Identifier renaming**
	renaming variables, classes, and functions to meaningless or misleading names

	eg. `getName()` -> `al3J4Nj()`
- **Control flow obfuscation**
	restructuring code to change execution order and make the logical flow appear confusing for readers
- **String encryption**
	encoding strings and decoding them at runtime
- **Dead code insertion**
	adding unused or fake code to bloat up the program to confuse readers
- **Self-modifying code**
	code that changes itself at runtime which is extremely difficult to trace
- **Opaque Predicates**
	replacing True/False statements with conditions that always evaluate to True/False

	eg.
	```if (user.isLoggedIn)```->
	```if (((123 * 123) % 2 == 1) && user.isLoggedIn)```
	
And more
### common tools

- **JavaScript**: Obfuscator.io, UglifyJS
- **Java**: ProGuard, DashO
- **.NET**: ConfuserEx, Dotfuscator
- **Python**: PyArmor, Nuitka (partial obfuscation), Cython

### Is Obfuscation enough?
The short answer is no.
Obfuscation is simply a deterrent, and it doesn't stop reverse engineering, but only slows it.
Obfuscation can usually be easily identified and skilled attackers can crack it if they REALLY wanted to, but it just takes longer.

Obfuscation is a layer of protection and (if your code seriously needs protecting) it should be combined with other methods like:

- encryption
- code signing (verifying that code hasn't been tampered)
- anti-debugging and tamper checks (to detect tools like debuggers or emulators)
