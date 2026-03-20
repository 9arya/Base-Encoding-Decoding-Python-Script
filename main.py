from fungsi import fungsi
from time import sleep
from termcolor import colored

while True:
  print("mau apa:\n1.base16\n2.base32\n3.base64\n4.base85\n5.keluar")
  try:
    pilihan = int(input(">>").strip())
    if pilihan == 1:
      sleep(0.02)
      fungsi(16)
    elif pilihan == 2:
      sleep(0.02)
      fungsi(32)
    elif pilihan == 3:
      sleep(0.02)
      fungsi(64)
    elif pilihan == 4:
      sleep(0.02)
      fungsi(85)
    elif pilihan == 5:
      sleep(0.001)
      break
    else:
      print(colored("pilihanmu tidak ada dalam daftar", "yellow"))
  except ValueError:
    print(colored("kamu memasukan hal yang tidak sesuai", "yellow"))
  except KeyboardInterrupt:
    print(colored("kalau keluar pakai opsi nomor 5", "red"))
  except EOFError:
    print(colored("\ngak boleh pakai ctrl + D ya", "red"))
