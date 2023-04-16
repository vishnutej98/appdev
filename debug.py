import getpass

USERDETAILS = {'vishnu': '1998', 'tej': '123'}


def get_username():
  username = input('Username: ').lower()
  return username


def get_password():
  password = getpass.getpass()
  return password


def verification(verify_name, name, password):
  # self.verifyname = verifyname
  # self.name = name
  # self.password = password
  if verify_name == name:
    print('name')
    verify_key = USERDETAILS[verify_name]
    if verify_key == password:
      print('key')
      return verify_name, verify_key
    else:
      # get_password()
      print('username password not match!!\nplease re-enter the verification details')
      username_verify()
  else:
    ...


def username_verify():
  name = get_username()
  password = get_password()
  for verify_name in USERDETAILS:
    verification(verify_name, name, password)
    # break


username_verify()