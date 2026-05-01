from fungsi import fungsi
from termcolor import colored

while True:
  print("pick algorithm:\n1.base16\n2.base32\n3.base64\n4.base85\n5.keluar")
  try:
    pilihan = int(input(">>").strip())
    if pilihan == 1:
      fungsi(16)
    elif pilihan == 2:
      fungsi(32)
    elif pilihan == 3:
      fungsi(64)
    elif pilihan == 4:
      fungsi(85)
    elif pilihan == 5:
      break
    else:
      print(colored("no one in options", "yellow"))
  except ValueError:
    print(colored("your input not valid", "yellow"))
  except KeyboardInterrupt:
    break
  except EOFError:
    break
