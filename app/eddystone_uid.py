#!/usr/bin/python
from argument_parser import parse
from beacon import Beacon
from utils import hexify, hex_split, exit_with


class EddystoneUid(Beacon):
    """
    Eddystone UID

    About:      general - https://github.com/google/eddystone/blob/master/protocol-specification.md
                uid     - https://github.com/google/eddystone/tree/master/eddystone-uid

    Example:    sudo python3 eddystone_uid.py -N eddystone -i uid

    Usage:      sudo python3 eddystone_uid.py [-N|--namespace=namespace (10-byte, default=fedcba9876)]
                                              [-i|--instance=instance (6-byte, default=123456)]
                                              [-p|--power=power (0-255, default=200)]
                                              [-d|--device=BLE device to use (default=hci0)]
                                              [-h|--help]
    """

    def __init__(self, **kwargs):
        self.namespace = kwargs["namespace"]
        self.instance = kwargs["instance"]
        super().__init__(**kwargs)

    def run(self):
        power_hex = hexify(self.power, 2)
        namespace_hex = hexify(self.namespace, 20)
        instance_hex = hexify(self.instance, 12)
        self.__print(namespace_hex, instance_hex, power_hex)

        frame_type = "00"
        eddystone = f"02 01 06 03 03 AA FE 15 16 AA FE {frame_type}"
        content = f"{hex_split(namespace_hex)} {hex_split(instance_hex)}"
        self._run_command(f"{eddystone} E7 {content}")

    def _validate(self):
        super()._validate()
        if len(self.namespace) > 10:
            exit_with(f"Error: invalid namespace! {self.namespace} is longer than 10-byte")
        if len(self.instance) > 6:
            exit_with(f"Error: invalid instance! {self.instance} is longer than 6-byte")

    def __print(self, namespace_hex, instance_hex, power_hex):
        print(f"Advertising on {self.device} with:")
        print(f"  namespace: {self.namespace} (0x{namespace_hex})")
        print(f"   instance: {self.instance} (0x{instance_hex})")
        print(f"      power: {self.power} (0x{power_hex})")


def main():
    beacon = EddystoneUid(**parse())
    beacon.run()


if __name__ == "__main__":
    main()
