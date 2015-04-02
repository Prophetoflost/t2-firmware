import sys
import usb.core

REQ_PWR  = 0x10

pins = {
    'rst': 0x0,
    'soc': 0x1,
    '1v8': 0x2,
    'a': 0x10,
    'b': 0x11,
    'led': 0x20,
}

dev = usb.core.find(idVendor=0x9999, idProduct=0xffff)
if dev is None:
    raise ValueError('device is not connected')

dev.ctrl_transfer(0x40, 0x10, int(sys.argv[2]), pins[sys.argv[1]], '')
