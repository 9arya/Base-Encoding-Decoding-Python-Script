import base64
import sys
import binascii
try:
    with open(sys.argv[1], "rb") as i:
        with open(sys.argv[2], "wb") as o:
            base64.decode(i, o)
except IndexError:
    print(f"use like:\npython {sys.argv[0]} input output\nfor example:\npython {sys.argv[0]} cat_picture.jpg cat_picture")
except FileNotFoundError:
    print(f"{sys.argv[1]} not found")
except binascii.Error:
    print("is not a encoded file")

