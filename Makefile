PYTHON ?= /opt/anaconda3/bin/python
PYTHON_ENV = PYTHONDONTWRITEBYTECODE=1

.PHONY: test audit audit-machine verify clean

test:
	$(PYTHON_ENV) $(PYTHON) -m unittest discover -s tests

audit:
	$(PYTHON_ENV) $(PYTHON) scripts/pacs.py audit --target . --json

audit-machine:
	$(PYTHON_ENV) $(PYTHON) scripts/pacs.py audit --target . --mode machine --json

verify: test audit audit-machine

clean:
	find . -name '__pycache__' -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
	find . -name '.DS_Store' -delete
