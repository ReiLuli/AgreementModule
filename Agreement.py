"""

Made by Rei Luli
Instagram : @reiluli.v2

Use this module to not get sued
(Feel free to modify it so it can fulfill ur needs)

if you don't know how to use python modules, make sure this file is saved on the same directory with you program
files then import "Agreement" and write "Agreement.agree()" on the line you wish this module to start.
Ps.: Make sure;
you have installed the module "colorama" (You can install this with PIP: pip install colorama (On windows) or : sudo
pip install colorama (On linux).

"""

import os
from colorama import Fore
def agree():
  print(Fore.WHITE + "The author is not responsible for damages caused by this program.")
  print('Please enter "Agree" if you agree that the author is not responsible for damages caused by this software and '
        'you take full responsibility')
  agreee = input(": ")
  if agreee == "Agree" or agreee == "agree" or agreee == "AGREE":
    print(Fore.GREEN + "ACCESS GRANTED")
  else:
      os.system("cls")
      print(Fore.RED + "ACCESS REFUSED")
      print(Fore.LIGHTYELLOW_EX + "Please enter " + Fore.LIGHTGREEN_EX + '"Agree"' + Fore.LIGHTYELLOW_EX + " to continue")
      agree()
      return agree
