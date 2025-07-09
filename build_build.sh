#!/bin/bash

# Build and install dependencies
pip install -r src/nfc-gate/requirements.txt
pip install -r src/ram-scraper/requirements.txt
pip install -r src/payment-bypass/requirements.txt

# Compile any necessary binaries (if needed)
# Example: gcc -o nfc-gate src/nfc-gate/nfc-gate.c
