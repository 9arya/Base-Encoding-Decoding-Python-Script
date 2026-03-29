#!/usr/bin/env python3
import sys
from base64 import *
import binascii
try:
    if len(sys.argv) < 4:
        print("usage:\npython3 cli.py en b16 hello word")
    else:
        mtden = {
                16: b16encode,
                32: b32encode,
                64: b64encode,
                85: b85encode
                }
        mtddec = {
                16: b16decode,
                32: b32decode,
                64: b64decode,
                85: b85decode
                }
        if sys.argv[1] == "en":
            if sys.argv[2] == "b16":
                a = " ".join(sys.argv[3:]).encode()
                b = mtden[16](a)
                print(b.decode())
            elif sys.argv[2] == "b32":
                a = " ".join(sys.argv[3:]).encode()
                b = mtden[32](a)
                print(b.decode())
            elif sys.argv[2] == "b64":
                a = " ".join(sys.argv[3:]).encode()
                b = mtden[64](a)
                print(b.decode())
            elif sys.argv[2] == "b85":
                a = " ".join(sys.argv[3:]).encode()
                b = mtden[85](a)
                print(b.decode())
            else:
                print("the algorithm is not support or not correct")
        elif sys.argv[1] == "dec":
            if sys.argv[2] == "b16":
                c = " ".join(sys.argv[3:]).encode()
                d = mtddec[16](c)
                print(d.decode())
            elif sys.argv[2] == "b32":
                c = " ".join(sys.argv[3:]).encode()
                d = mtddec[32](c)
                print(d.decode())
            elif sys.argv[2] == "b64":
                c = " ".join(sys.argv[3:]).encode()
                d = mtddec[64](c)
                print(d.decode())
            elif sys.argv[2] == "b85":
                c = " ".join(sys.argv[3:]).encode()
                d = mtddec[85](c)
                print(d.decode())
            else:
                print("the algorithm is not support or not correct")
except SyntaxError:
    print("yang ngoding gak bener")
except binascii.Error:
    print("your encode message is not same with the algorithm your pick")
except UnicodeDecodeError:
    print("are you use not encoded text in decode options?")
