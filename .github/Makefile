.PHONY : all ci_rustlings_check dependencies

PYTHON := python3
PIP := pip3

all:
	@echo "CI Build System"

CI_RUSTLINGS_CHECK_PATH := scripts/rustlings_check.py

ci_rustlings_check: dependencies
	@$(PYTHON) $(CI_RUSTLINGS_CHECK_PATH)

LIB_PYTHON_TOML := toml

dependencies:
	@if ! $(PIP) show $(LIB_PYTHON_TOML) > /dev/null 2>&1; then \
		$(PIP) install $(LIB_PYTHON_TOML) > /dev/null 2>&1; \
	fi
