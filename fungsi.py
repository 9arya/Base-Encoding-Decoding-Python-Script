from base64 import b32encode, b32decode, b64decode, b64encode, b16decode, b16encode, b85encode, b85decode
from termcolor import colored
import binascii
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
    print("pilih program:\n1.encode\n2.decode\n3.kembali")
    try:
      pilih = int(input(">>").strip())
      if pilih == 1:
        pesan = input("ketik pesannya:").encode("UTF-8")
        print("hasilnya:\n")
        print(colored(metodeen[tipe](pesan).decode("UTF-8"), "green"))
      elif pilih == 2:
        kode = input("apa kodenya:").encode("UTF-8")
        print("hasilnya:\n")
        print(colored(metodede[tipe](kode).decode("UTF-8"), "blue"))
        print("\n")
      elif pilih == 3:
        print("menghentikan program")
        break 
      else:
        print(colored("masukanmu salah", "red"))
    except ValueError:
      print(colored("masukan tidak benar", "red"))
    except binascii.Error:
      print("yah eror")
    except KeyboardInterrupt:
      print(colored("kalau mau berhenti pilih opsi ke 3 jangan pakai ctrl + c", "yellow"))
    except EOFError:
      print(colored("sebaiknya pakai opsi nomor 3 kalau mau pergi", "yellow"))
