# beacon-emulator

This repository is based on [linux-ibeacon][LINUX IBEACON] by [dburr][DBURR]. 
It allows the emulation of different beacon formats:

* iBeacon
* Eddystone-UID
* Kontakt Scan Response

## iBeacon

### About
      
* [Information about iBeacon][IBEACON]

### Example

```
sudo python3 ibeacon.py -u ffffffff-bbbb-cccc-dddd-eeeeeeeeeeee -M 13 -m 12
```

### Usage:      
 
```   
sudo python3 ibeacon.py [-u|--uuid=<UUID> (default=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee)]
                        [-M|--major=<major> (0-65535, default=0)]
                        [-m|--minor=<minor> (0-65535, default=0)]
                        [-p|--power=<power> (0-255, default=200)]
                        [-d|--device=<BLE device to use> (default=hci0)]
                        [-h|--help]
```

## Eddystone UID

### About
 
* [General information about Eddystone][EDDYSTONE]
* [Information about the type Eddystone-UID][EDDYSTONE UID]

### Example

```
sudo python3 eddystone_uid.py -N eddystone -i uid
```

### Usage
      
```
sudo python3 eddystone_uid.py [-N|--namespace=namespace (10-byte, default=fedcba9876)]
                              [-i|--instance=instance (6-byte, default=123456)]
                              [-p|--power=power (0-255, default=200)]
                              [-d|--device=BLE device to use (default=hci0)]
                              [-h|--help]
```

## Kontakt

### About
      
* [Information about Kontakt Scan Response]

### Example

```    
sudo python3 kontakt.py -a Kontakt
```

### Usage

```     
sudo python3 kontakt.py [-a|--advertisement=advertisement (10-byte, default=fedcba9876)]
                        [-p|--power=power (0-255, default=200)]
                        [-d|--device=BLE device to use (default=hci0)]
                        [-h|--help]
```

License
-------

This repository is licensed under the [MIT license][MITLICENSE].

Copyright 2019 Wolfhard Fehre

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[LINUX IBEACON]: https://github.com/dburr/linux-ibeacon "linux ibeacon repository"
[DBURR]: https://github.com/dburr "dburr"
[IBEACON]: https://developer.kontakt.io/hardware/packets/ibeacon/ "iBeacon"
[EDDYSTONE]: https://github.com/google/eddystone/blob/master/protocol-specification.md "Eddystone"
[EDDYSTONE UID]: https://github.com/google/eddystone/tree/master/eddystone-uid "Eddystone-UID"
[KONTAKT SCAN RESPONSE]: https://developer.kontakt.io/hardware/packets/scanresponse/ "Kontakt Scan Response"
[MITLICENSE]: http://opensource.org/licenses/MIT "MIT License"
