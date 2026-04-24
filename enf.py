import base64
import sys
try:
    with open(sys.argv[1], "rb") as f:
        with open(sys.argv[2], "wb") as i:
            x = base64.encode(f, i)
except IndexError:
    print(f"use with name of file in format:\npython {sys.argv[0]} file\nfor example:\npython {sys.argv[0]} mytext.txt")
except FileNotFoundError:
    print(f"{sys.argv[1]} not found")
