run:
	@echo "\n\nOBFUSCATED CODE\n\n"
	@python3 obfuscator.py $(ARGS) > result.py
	@echo "\n\nRUNNING RESULTANT OBFUSCATED CODE\n\n"
	@python3 result.py

run-lazy:
	@echo "\n\nOBFUSCATED CODE\n\n"
	@python3 obfuscator.py testingCodeFiles/testInput.py -v achilles > result.py
	@echo "\n\nRUNNING RESULTANT OBFUSCATED CODE\n\n"
	@python3 result.py
