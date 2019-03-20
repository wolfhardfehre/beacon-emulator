#!/usr/bin/python
import re
import os
import sys
import uuid
import binascii

UUID_MATCH = re.compile('^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$', re.I)


def get_random_uuid():
    return uuid.uuid4().hex


def hexify(i, digits=2):
    if isinstance(i, int):
        return format(i, f"0{digits}x").upper()
    elif isinstance(i, str):
        encoded = i.encode()
        hexadecimal = binascii.hexlify(encoded)
        upper = hexadecimal.upper()
        zero_filled = upper.zfill(digits)
        return zero_filled.decode()


def hex_split(string):
    return ' '.join([string[i:i + 2] for i in range(0, len(string), 2)])


def process_command(c):
    os.system(c)


def exit_with(message):
    print(message)
    sys.exit(1)


def is_sudo():
    return 1 if "SUDO_UID" in os.environ.keys() else 0


def is_unsigned_int(value):
    return 0 <= value <= 65535


def is_uuid(uuid):
    return UUID_MATCH.match(uuid)


def is_valid_device(device):
    return not os.system(f"hciconfig list 2>/dev/null | grep -q ^{device}:")
