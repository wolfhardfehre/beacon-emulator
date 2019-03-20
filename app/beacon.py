from abc import ABC, abstractmethod
from utils import process_command, is_valid_device, exit_with


class Beacon(ABC):

    def __init__(self, **kwargs):
        self.device = self.__device(kwargs["device"])
        self.power = int(kwargs["power"])
        self._validate()
        self.head_cmd = f"hcitool -i {self.device} cmd 0x08 0x0008 1E"
        self.tail_cmd = "00 >/dev/null"

    def _run_command(self, cmd):
        process_command(f"hciconfig {self.device} up")
        process_command(f"hciconfig {self.device} leadv")
        process_command(f"hciconfig {self.device} noscan")
        process_command(f"{self.head_cmd} {cmd} {self.tail_cmd}")
        process_command(f"sudo hcitool -i hci0 cmd 0x08 0x0006 a0 00 a0 00 03 00 00 00 00 00 00 00 00 07 {self.tail_cmd}")

    def _validate(self):
        if not is_valid_device(self.device):
            exit_with(f"Error: no such device: {self.device} (try `hciconfig list')")

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @staticmethod
    def __device(temp_device):
        return f"hci{temp_device}" if not temp_device.startswith("hci") else temp_device
