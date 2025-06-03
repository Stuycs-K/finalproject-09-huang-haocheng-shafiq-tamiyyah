run:
	@python3 obfuscator.py $(ARGS)

run-lazy:
	@python3 obfuscator.py testingCodeFiles/testInput.py output.txt -v None
