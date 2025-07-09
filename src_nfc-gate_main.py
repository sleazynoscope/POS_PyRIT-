import nfc
import time

def nfc_relay():
    clf = nfc.ContactlessFrontend('usb')
    while True:
        clf.connect(rdwr={'on-connect': lambda tag: tag.dump()})
        time.sleep(1)

if __name__ == "__main__":
    nfc_relay()
