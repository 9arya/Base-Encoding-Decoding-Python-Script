#!/usr/bin/env python3
import sys
from base64 import *
import binascii
print("\n")
a = " ".join(sys.argv[3:]).encode()
try:
    if len(sys.argv) < 4:
        print("usage:\nbed en b16 hello word")
    else:
        mtden = {
                "b16": b16encode,
                "b32": b32encode,
                "b32hex": b32hexencode,
                "b64": b64encode,
                "b85": b85encode,
                "z85": z85encode
                }
        mtddec = {
                "b16": b16decode,
                "b32": b32decode,
                "b32hex": b32hexdecode,
                "b64": b64decode,
                "b85": b85decode,
                "z85": z85decode
                }
        if sys.argv[1] == "en":
            if sys.argv[2] in mtden:
                b = mtden[sys.argv[2]](a)
                print(b.decode())
            else:
                print("the algorithm not support or incorrect")
        elif sys.argv[1] == "dec":
            if sys.argv[2] in mtddec:
                c = mtddec[sys.argv[2]](a)
                print(c.decode())
            else:
                print("the algorithm is not support or not correct")
except SyntaxError:
    print("yang ngoding gak bener")
except binascii.Error:
    print("your encode message is not same with the algorithm your pick")
except UnicodeDecodeError:
    print("are you use not encoded text in decode options?")
finally:
    print("\n")
