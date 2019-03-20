#!/usr/bin/python
from argument_parser import parse
from beacon import Beacon
from utils import is_sudo, hex_split, hexify, exit_with, is_uuid, is_unsigned_int


class IBeacon(Beacon):
    """
    iBeacon

    About:      https://developer.kontakt.io/hardware/packets/ibeacon/

    Example:    sudo python3 ibeacon.py -u ffffffff-bbbb-cccc-dddd-eeeeeeeeeeee -M 13 -m 12

    Usage:      sudo python3 ibeacon.py [-u|--uuid=<UUID> (default=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee)]
                                        [-M|--major=<major> (0-65535, default=0)]
                                        [-m|--minor=<minor> (0-65535, default=0)]
                                        [-p|--power=<power> (0-255, default=200)]
                                        [-d|--device=<BLE device to use> (default=hci0)]
                                        [-h|--help]
    """

    def __init__(self, **kwargs):
        self.major = int(kwargs["major"])
        self.minor = int(kwargs["minor"])
        self.uuid = kwargs["uuid"]
        super().__init__(**kwargs)

    def run(self):
        power_hex = hexify(self.power, 2)
        major_hex = hexify(self.major, 4)
        minor_hex = hexify(self.minor, 4)
        self.__print(major_hex, minor_hex, power_hex)

        content = f"{self.__uuid()} {hex_split(major_hex)} {hex_split(minor_hex)} {power_hex}"
        manufacturer = "4C 00 02 15"
        ibeacon = f"02 01 06 1A FF {manufacturer}"
        self._run_command(f"{ibeacon} {content}")

    def _validate(self):
        super()._validate()
        if not is_uuid(self.uuid):
            exit_with(f"Error: `{self.uuid}' is an invalid UUID.")
        if not is_unsigned_int(self.major):
            exit_with("Error: major id is out of bounds (0-65535)")
        if not is_unsigned_int(self.minor):
            exit_with("Error: minor id is out of bounds (0-65535)")
        if not is_sudo():
            exit_with("Error: this script requires superuser privileges.  Please re-run with `sudo.'")

    def __uuid(self):
        uuid = self.uuid.replace("-", "").upper()
        return hex_split(uuid)

    def __print(self, major_hex, minor_hex, power_hex):
        print(f"Advertising on {self.device} with:")
        print(f"         uuid: {self.uuid}")
        print(f"  major/minor: {self.major}/{self.minor} (0x{major_hex}/0x{minor_hex})")
        print(f"        power: {self.power} (0x{power_hex})")


def main():
    beacon = IBeacon(**parse())
    beacon.run()


if __name__ == "__main__":
    main()
