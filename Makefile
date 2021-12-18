.PHONY: dependency
dependency:
	@pip install -r requirements.txt

.PHONY: run
run:
	@python3 main.py > result.csv