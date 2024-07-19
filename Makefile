PYTHON = python3.12

VENV_DIR = venv
REQ_FILE = pyproject.toml
SRC_DIR = scripts
TEST_DIR = test

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -U pip
	$(VENV_DIR)/bin/pip install poetry
	$(VENV_DIR)/bin/poetry install

.PHONY: install
install: venv
	$(VENV_DIR)/bin/poetry install

.PHONY: test
test:
	$(VENV_DIR)/bin/pytest --cov=$(SRC_DIR) --cov-report=term-missing

.PHONY: coverage
coverage:
	$(VENV_DIR)/bin/pytest --cov=$(SRC_DIR) --cov-report=html

.PHONY: run
run:
	$(VENV_DIR)/bin/python $(SRC_DIR)/run.py

.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov

.PHONY: pre-commit
pre-commit:
	$(VENV_DIR)/bin/pre-commit install
