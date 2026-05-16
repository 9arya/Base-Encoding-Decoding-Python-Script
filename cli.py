#!/usr/bin/env python3
#BSD 3-Clause License
#
#Copyright (c) 2025, 9arya
import base64
import binascii
import sys

print("\n")
try:
    if len(sys.argv) < 4:
        print("usage:\nbed en b16 hello word")
    else:
        mtden = {
                "b16": base64.b16encode,
                "b32": base64.b32encode,
                "b32hex": base64.b32hexencode,
                "b64": base64.b64encode,
                "b85": base64.b85encode,
                "z85": base64.z85encode
                }
        mtddec = {
                "b16": base64.b16decode,
                "b32": base64.b32decode,
                "b32hex": base64.b32hexdecode,
                "b64": base64.b64decode,
                "b85": base64.b85decode,
                "z85": base64.z85decode
                }
        a = " ".join(sys.argv[3:]).encode()
        if sys.argv[1] == "en" or sys.argv[1] == "encode" or sys.argv[1] == "e":
            if sys.argv[2] in mtden:
                b = mtden[sys.argv[2]](a)
                print(b.decode())
            else:
                print("the algorithm not support or incorrect")
        elif sys.argv[1] == "de" or sys.argv[1]=="d" or sys.argv[1] == "decode":
            if sys.argv[2] in mtddec:
                c = mtddec[sys.argv[2]](a)
                print(c.decode())
            else:
                print("the algorithm is not support or not correct")
        else:
            print(f"{sys.argv[1]} not in method,this tools only support encode and decode")
except SyntaxError:
    print("yang ngoding gak bener")
except binascii.Error:
    print("your encode message is not same with the algorithm your pick")
except UnicodeDecodeError:
    print("are you use not encoded text in decode options?")
finally:
    print("\n")
