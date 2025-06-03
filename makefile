run:
	@echo "\nOBFUSCATED CODE\n"
	@python3 obfuscator.py $(ARGS)
	@python3 obfuscator.py $(ARGS) > result.py
	@echo "\nRUNNING RESULTANT OBFUSCATED CODE\n"
	@python3 result.py

run-lazy:
	@echo "\ORIGGINAL CODE\n"
	@python3 testingCodeFiles/testInput.py
	@echo "\nOBFUSCATED CODE\n"
	@python3 obfuscator.py testingCodeFiles/testInput.py -v achilles > result.py
	@python3 obfuscator.py $(ARGS) > result.py
	@echo "\nRUNNING RESULTANT OBFUSCATED CODE\n"
	@python3 result.py
