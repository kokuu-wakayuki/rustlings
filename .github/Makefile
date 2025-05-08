.PHONY : all ci_rustlings_check dependencies

CARGO := cargo
RUSTLINGS := rustlings
PYTHON := python3
PIP := pip3

all:
	@echo "CI Build System"

CI_RUSTLINGS_CHECK_PATH := scripts/rustlings_check.py

ci_rustlings_check: dependencies
	@$(PYTHON) $(CI_RUSTLINGS_CHECK_PATH)

LIB_PYTHON_TOML := toml

dependencies:
	@if ! command -v $(RUSTLINGS) > /dev/null; then \
		$$(CARGO) install $(RUSTLINGS); \
	fi
	@if ! $(PIP) show $(LIB_PYTHON_TOML); then \
		$(PIP) install $(LIB_PYTHON_TOML); \
	fi
