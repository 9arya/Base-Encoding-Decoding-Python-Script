#BSD 3-Clause License
#
#Copyright (c) 2025, 9arya
import base64
import sys
import binascii
def main():
    try:
        if len(sys.argv) <= 2:
            while True:
                metode = input("pilih salah satu:\n1.encode\n2.decode\n>")
                if metode == "" or metode == "\n":
                    print("tolong pilih salah satu")
                elif metode != "1" and metode != "2":
                    print("pilih yang ada dipilihan!")
                else:
                    break
            pesan = input("ketik pesanmu:")
            bp = pesan.encode()
            if metode == "1":
                bhasil = base64.b16encode(base64.b32encode(base64.b64encode(bp)))
                hasil = bhasil.decode()
                print(hasil)
                return
            elif metode == "2":
                bhasil = base64.b64decode(base64.b32decode(base64.b16decode(bp)))
                hasil = bhasil.decode()
                print(hasil)
                return
        else:
            pesan = (" ".join(sys.argv[2:])).encode()
            if sys.argv[1] == "en" or sys.argv[1] == "encode" or sys.argv[1] == "1":
                hasil = (base64.b16encode(base64.b32encode(base64.b64encode(pesan)))).decode()
                print(hasil)
                return
            elif sys.argv[1] == "dec" or sys.argv[1]=="decode" or sys.argv[1]=="2":
                hasil = (base64.b64decode(base64.b32decode(base64.b16decode(pesan)))).decode()
                print(hasil)
    except (EOFError, KeyboardInterrupt):
        return
    except (binascii.Error, ValueError):
        print("wow,kamu memasukan input yang tidak valid dalam metode decode")
if __name__=="__main__":
    main()
