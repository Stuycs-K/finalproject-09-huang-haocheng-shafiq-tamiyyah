run:
	@echo "\nOBFUSCATED CODE\n"
	@python3 obfuscator.py $(ARGS)
	@python3 obfuscator.py $(ARGS) > result.py
	@expand -t 4 result.py | tee result.py
	@echo "\nRUNNING RESULTANT OBFUSCATED CODE\n"
	@python3 result.py

run-lazy:
	@echo "\nORIGINAL CODE\n"
	@cat testingCodeFiles/testInput.py
	@echo "\nOBFUSCATED CODE\n"
	@python3 obfuscator.py testingCodeFiles/testInput.py -v achilles > result.py
	@python3 obfuscator.py testingCodeFiles/testInput.py -v achilles
	@echo "\nRUNNING RESULTANT OBFUSCATED CODE\n"
	@python3 result.py
	@echo "\nRUNNING ORIGINAL CODE\n"
	@python3 testingCodeFiles/testInput.py
