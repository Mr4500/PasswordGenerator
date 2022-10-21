#imports
import PasswordGenerator
import CSVCode


def WelcomeMenu():
  #Choose an option
  WelcomeOption = input("Welcome to Matthew's Password Generator\n\nPlease select one of the following options:\n\n1: Generate Password\n2: Account Details and Random Password\n3: Search for PasswordID\n4: Exit\n\n>")
  WelcomeOptionsLoop = True
  #takes you to the desired option
  while WelcomeOptionsLoop == True:
    if WelcomeOption == "1":
      PasswordGenerator.GeneratePassword()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "2":
      AccountDetailsPassword()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "3":
      SearchAccountID()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "4":
      exit()
      WelcomeOptionsLoop = False
    else:
      WelcomeOptionsLoop = True

def AccountDetailsPassword():
    PasswordRegenerateLoop = True
    while PasswordRegenerateLoop == True:
      PasswordRegenerate = input("\nDo you want to regenerate your password? (Y/N)\n\n> ")
      if PasswordRegenerate.upper() == "Y":
        PasswordRegenerateLoop = False
      elif PasswordRegenerate.upper() == "N":
        PasswordRegenerateLoop = False
        GenerateLoop = False

        SavePasswordLoop = True
        while SavePasswordLoop == True:
          SavePasswordOption = input("\nDo you Want to save your details to our database? (Y/N)\n\n>")
          if SavePasswordOption.upper() == "Y":
            CSVCode.AddToCSV()
            print("\nYour details has now been saved")
            SavePasswordLoop = False
            PasswordRegenerateLoop = False
            MenuOption()
          elif SavePasswordOption.upper() == "N":
            print("\nWe have not saved your password")
            PasswordRegenerateLoop = False
            SavePasswordLoop = False
            MenuOption()
          else:
            SavePasswordLoop = True
      else:
        PasswordRegenerateLoop = True
        print("\nPlease choose an option")

WelcomeMenu()