#!/usr/bin/env python3

from soldiers import Soldier

def create_soldier(svc_num, rank, name, unit, corps):
  new_soldier = Soldier(svc_num, rank, name, unit, corps)
  return new_soldier

def save_soldier(soldier):
  soldier.save_soldier()

def list_soldiers():
  return Soldier.display_soldiers()

def remove_soldier(soldier):
  return soldier.delete_soldier()

def find_soldier(number):
  return Soldier.find_by_svcNumber(number)

def check_soldier_exists(number):
  return Soldier.check_if_exists(number)

def copy_soldier_svcNumber(number):
  return Soldier.copy_svcNumber(number)

def main():

  print("Hello, welcome to Atlas Private Corporation Systems v1.0.0")
  print("Please enter your name:")
  print('\n')
  user_name = input().capitalize()

  while True:
    print('\n')
    print(f"Hello {user_name}. Use the following keys to interact with the system: \n 1 - add a new soldier \n 2 - delete a soldier \n 3 - list all soldiers \n 4 - find a soldier \n 5 - copy a soldier's service number \n 6 - exit the system")

    try:
      short_code = int(input())

      if short_code == 1:
        print('\n')
        print("Creating a new soldier...")
        
        print("Enter the service number...")
        try:
          s_num = int(input())
        except ValueError:
          print("Please use numbers")

        print("Enter the rank...")
        s_rank = input().capitalize()

        print("Enter the name...")
        s_name = input().capitalize()

        print("Enter the unit...")
        s_unit = input().upper()

        print("Enter the corps...")
        s_corps = input().upper()
        print('\n')
        print(f"New soldier added:\n name:{s_name}, service number: {s_num}")

        save_soldier(create_soldier(s_num, s_rank, s_name, s_unit, s_corps))

        print('\n')

      elif short_code == 2:
        print('\n')
        print("Option 2")
        print('\n')

      elif short_code == 3:
        print('\n')
        
        if list_soldiers():
          print("Here is a list of all the soldiers:")
          print('\n')

          for soldier in list_soldiers():
            print(f"{soldier.svc_num} {soldier.rank} {soldier.name} {soldier.unit} {soldier.corps}")
            print('\n')

        else:
          print("Sorry, there are no soldiers in this list yet")    

        print('\n')

      elif short_code == 4:
        print('\n')
        print("Enter the service number of the soldier you wish to find")
        
        try:
          search_number = int(input())
        except ValueError:
          print("Please enter a number")

        if check_soldier_exists(search_number):
          found_soldier = Soldier.find_by_svcNumber(search_number)
          print("Here's the soldier you're looking for...")
          print(f"{found_soldier.svc_num} {found_soldier.rank} {found_soldier.name} {found_soldier.unit} {found_soldier.corps}")
          print('\n')
        else:
          print("Sorry, that soldier is not in our list")

      elif short_code == 5:
        print('\n')
        print("Option 5")
        print('\n')

      elif short_code == 6:
        print('\n')
        print("existing the system...have a nice day")
        print('\n')
        break
      else:
        print('\n')
        print("Please use the numbers 1 - 6")
        print('\n')
    except ValueError:
      print('\n')
      print("Please use the numbers 1 - 6")
      print('\n')
if __name__ == '__main__':
  main()