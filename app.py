#!Python3
#First instance of the application
#Creating an app login backend verification

#importing the required libraries
import getpass

#Dictionary for storing the user the details
USERDETAILS = {'Vishnu':'1998', 'Tej':'123'}

def main():
  username = input("Username: ").title()
  password = getpass.getpass("Password: ")
  for i in USERDETAILS.keys():
    if username == i:
      while password != USERDETAILS.get(i):
        password = getpass.getpass("Enter the correct password: ")

      break
  print("Verified!")
  

if __name__ == '__main__':
  main()