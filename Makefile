# Makefile for Kasparro Backend & ETL Systems Assignment

# Variables
PYTHON = python3
PIP = pip3
ENV_FILE = .env
DATABASE_URL = sqlite:///./dev.db
UVICORN = uvicorn
APP_MODULE = app.main:app

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  setup        Install dependencies"
	@echo "  run          Start FastAPI server"
	@echo "  run-etl      Run ETL script"
	@echo "  test         Run tests"
	@echo "  migrate      Run Alembic migrations"
	@echo "  clean        Remove __pycache__ and temp files"

# Install dependencies
setup:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run FastAPI server
run:
	$(UVICORN) $(APP_MODULE) --host 0.0.0.0 --port 8000 --reload

# Run ETL
run-etl:
	$(PYTHON) scripts/run_etl.py

# Run tests
test:
	pytest tests/

# Run Alembic migrations
migrate:
	alembic upgrade head

# Clean pycache and temp files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.pyc
