#!Python3
#First instance of the application
#Creating an app login backend verification

#importing the required libraries
import getpass

#Dictionary for storing the user the details
USERDETAILS = {'Vishnu':'1998', 'tej':'123'}

class details():
  def get_username():
    username = input('Username: ').lower()
    return username
  

  def get_password():
    password = getpass.getpass()
    return password


  def verification(verify_name, name, password):
    if verify_name.lower() == name.lower():
      print("User found in data base...")
      verify_key = USERDETAILS[verify_name]
      if verify_key == password:
        print('Login successfull')
        return (verify_name, verify_key)
      else:
        print("Username and Password doesn't match\nRe-enter the credentials")
        main()
    else:
      # print("Username and Password doesn't match\nRe-enter the credentials")
      # main()
      ...


def main():
  name = details.get_username()
  password = details.get_password()
  for verify_name in USERDETAILS:
    details.verification(verify_name, name, password)

  
  print('Press Q or q button to exit')
  if input('').lower() == 'q':
    #Do nothing
    exit
  else:
    main()
  

if __name__ == '__main__':
  main()