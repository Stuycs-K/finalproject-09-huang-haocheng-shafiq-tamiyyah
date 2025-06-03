run:
	@python3 obfuscate.py $(ARGS)

run-lazy:
	@python3 obfuscate.py testingCodeFiles/testInput.py output.txt -v None
