import sys
import getopt

FLAGS = "hu:M:m:p:d:N:i:a:"
ARGUMENTS = ["help", "uuid=", "major=", "minor=", "power=", "device=", "namespace=", "instance=", "advertisement="]
DEFAULT_ARGUMENTS = {
    "device": "hci0",
    "uuid": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "major": 0,
    "minor": 0,
    "namespace": "fedcba9876",
    "instance": "123456",
    "advertisement": "Kontakt",
    "power": 200
}


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def parse(argv=None):
    kwargs = DEFAULT_ARGUMENTS
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], FLAGS, ARGUMENTS)
        except getopt.error as msg:
            raise Usage(msg)

        for o, a in opts:
            if o in ("-h", "--help"):
                print(__doc__)
                sys.exit(0)
            elif o in ("-u", "--uuid"):
                kwargs["uuid"] = a
            elif o in ("-M", "--major"):
                kwargs["major"] = a
            elif o in ("-m", "--minor"):
                kwargs["minor"] = a
            elif o in ("-p", "--power"):
                kwargs["power"] = a
            elif o in ("-d", "--device"):
                kwargs["device"] = a
            elif o in ("-N", "--namespace"):
                kwargs["namespace"] = a
            elif o in ("-i", "--instance"):
                kwargs["instance"] = a
            elif o in ("-a", "--advertisement"):
                kwargs["advertisement"] = a

        return kwargs

    except Usage as err:
        print() >> sys.stderr, err.msg
        print() >> sys.stderr, "for help use --help"
        return sys.exit(2)
