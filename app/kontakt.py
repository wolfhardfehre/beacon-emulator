#!/usr/bin/python
from argument_parser import parse
from beacon import Beacon
from utils import hexify, hex_split, exit_with


class Kontakt(Beacon):
    """
    Kontakt

    About:      https://developer.kontakt.io/hardware/packets/scanresponse/

    Example:    sudo python3 kontakt.py -a Kontakt

    Usage:      sudo python3 kontakt.py [-a|--advertisement=advertisement (10-byte, default=fedcba9876)]
                                        [-p|--power=power (0-255, default=200)]
                                        [-d|--device=BLE device to use (default=hci0)]
                                        [-h|--help]
    """

    def __init__(self, **kwargs):
        self.advertisement = kwargs["advertisement"]
        super().__init__(**kwargs)

    def run(self):
        power_hex = hexify(self.power, 2)
        ad_hex = hexify(self.advertisement)
        self.__print(ad_hex, power_hex)
        length = hexify(len(hex_split(ad_hex).split(" ")) + 1)
        content = f"{length} 09 {hex_split(ad_hex)} 02 0A F4 0A 16 0D D0 61 62 63 64 04 02 06 00"
        self._run_command(content)

    def _validate(self):
        super()._validate()
        if len(self.advertisement) > 16:
            exit_with(f"Error: invalid advertisement! {self.advertisement} is longer than 16-byte")

    def __print(self, ad_hex, power_hex):
        print(f"Advertising on {self.device} with:")
        print(f"  advertisement: {self.advertisement} (0x{ad_hex})")
        print(f"          power: {self.power} (0x{power_hex})")


def main():
    beacon = Kontakt(**parse())
    beacon.run()


if __name__ == "__main__":
    main()
