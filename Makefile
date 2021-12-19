.PHONY: dependency
dependency:
	@pip3 install -r requirements.txt

.PHONY: run
run:
	@python3 main.py > result.csv