import binascii
from base64 import (b16decode, b16encode, b32decode, b32encode, b64decode,
                    b64encode, b85decode, b85encode)

from termcolor import colored


def fungsi(tipe):
  metodeen ={
    85: b85encode,
    64: b64encode,
    32: b32encode,
    16: b16encode
  }
  metodede = {
    85: b85decode,
    64: b64decode,
    32: b32decode,
    16: b16decode
  }
  if tipe not in metodede:
    return
  while True:
    print("pick program:\n1.encode\n2.decode\n3.back")
    try:
      pilih = int(input(">>").strip())
      if pilih == 1:
        pesan = input("write your message:").encode("UTF-8")
        print("you got this:\n")
        print(colored(metodeen[tipe](pesan).decode("UTF-8"), "green"))
      elif pilih == 2:
        kode = input("write the code:").encode("UTF-8")
        print("you got this:\n")
        print(colored(metodede[tipe](kode).decode("UTF-8"), "blue"))
        print("\n")
      elif pilih == 3:
        break 
      else:
        print(colored("no one in the options", "red"))
    except ValueError:
      print(colored("the input is not valid", "red"))
    except binascii.Error:
      print("wow you got an error,report it to developer")
    except KeyboardInterrupt:
        return
    except EOFError:
        return
