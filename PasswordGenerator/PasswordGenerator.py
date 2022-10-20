#imports
import random as random
from random_word import RandomWords

#Naming The Imports
RWG = RandomWords()
RNG = random

def Password123():
  #Loops the password generation if new password wanted
  GenerateLoop = True
  while GenerateLoop == True:
    #Generate and print Random Number 1
    RN1 = random.randint(10, 99)
    #Generate and print Random Word 1
    RW1 = RWG.get_random_word()
    #Generate and print Random Word 2
    RW2 = RWG.get_random_word()
    #Generate and print Random Number 2
    RN2 = random.randint(10, 99)

    SpecialCharacters = ("`", "¬", "!", '"', "£", "$", "%", "^", "&", "*", "(",
                         ")", "-", "=", "_", "+", "{", "}", "[", ']', ";", "'",
                         "#", ":", "@", "~", ".", "/", "<", ">", "?", "|")
    SC = random.choice(SpecialCharacters)
    Password = (f"{RN1}{RW1.capitalize()}{RW2.capitalize()}{RN2}{SC}")
    print("\nYour New password is:", Password)
    GenerateLoop = False

def AddToCSV(Email,AccountType,Username,Password,PasswordID):
  WritetoCSV = open("Database.csv","a")
  WritetoCSV.write(f"{Email},{AccountType},{Username},{Password},{PasswordID}\n")
  WritetoCSV.close()

def PasswordGenerator(Email,AccountType,Username):
  #Loops the password generation if new password wanted
  GenerateLoop = True
  while GenerateLoop == True:
    #Generate and print Random Number 1
    RN1 = random.randint(10, 99)
    #Generate and print Random Word 1
    RW1 = RWG.get_random_word()
    #Generate and print Random Word 2
    RW2 = RWG.get_random_word()
    #Generate and print Random Number 2
    RN2 = random.randint(10, 99)

    SpecialCharacters = ("`", "¬", "!", '"', "£", "$", "%", "^", "&", "*", "(",
                         ")", "-", "=", "_", "+", "{", "}", "[", ']', ";", "'",
                         "#", ":", "@", "~", ".", "/", "<", ">", "?", "|")
    SC = random.choice(SpecialCharacters)
    Password = (f"{RN1}{RW1.capitalize()}{RW2.capitalize()}{RN2}{SC}")
    print("\nYour New password is:", Password)
    PasswordID = random.randint(100000, 999999)
    PasswordID = (f"#{PasswordID}")
    print(f"Your Passord ID is: {PasswordID}")

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
            AddToCSV(Email,AccountType,Username,Password,PasswordID)
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

def AskUsername(Email,AccountType):
  UsernameLoop = True
  while UsernameLoop == True:
    Username = input("\nWhat is the Username linked to the account?\n\n> ")
    CorrectUser = input(f"Is this the correct username? {Username}\n\n> ")
    if CorrectUser.upper() == "Y":
      PasswordGenerator(Email,AccountType,Username)
      UsernameLoop = False
    elif CorrectUser.upper() == "N":
      UsernameLoop = True
    else:
      UsernameLoop = True

def AskAccount(Email):
  AccountTypeLoop = True
  while AccountTypeLoop == True:
    AccountType = input("\nWhat type of account is this? (e.g. Microsoft)\n\n> ")
    CorrectAccount = input(f"Is this the correct account type? {AccountType}\n\n> ")
    if CorrectAccount.upper() == "Y":
      AskUsername(Email,AccountType)
      AccountTypeLoop = False
    elif CorrectAccount.upper() == "N":
      AccountTypeLoop = True
    else:
      AccountTypeLoop = True

def AskEmail():
  EmailLoop = True
  while EmailLoop == True:
    Email = input("\nWhat is the Email linked to the account?\n\n> ")
    CorrectEmail = input(f"Is this the correct Email? {Email}\n\n> ")
    if CorrectEmail.upper() == "Y":
      AskAccount(Email)
      EmailLoop = False
    elif CorrectEmail.upper() == "N":
      EmailLoop = True
    else:
      EmailLoop = True

def MenuOption():
  MenuOptionLoop = True
  while MenuOptionLoop == True:
    MenuOption = input("\nWould you like to go back to the menu?\n\n>")
    if MenuOption.upper() == "Y":
      print("")
      WelcomeMenu()
    elif MenuOption.upper() == "N":
      exit()
    else:
      MenuOptionLoop = True

def WelcomeMenu():
  #Choose an option
  WelcomeOption = input("Welcome to Matthew's Password Generator\n\nPlease select one of the following options:\n\n1: Generate Password\n2: Save Deatils with Account\n3: Search for PasswordID\n4: Exit\n\n>")
  WelcomeOptionsLoop = True
  #takes you to the desired option
  while WelcomeOptionsLoop == True:
    if WelcomeOption == "1":
      Password123()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "2":
      AskEmail()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "3":
      SearchAccountID()
      WelcomeOptionsLoop = False
    elif WelcomeOption == "4":
      exit()
      WelcomeOptionsLoop = False
    else:
      WelcomeOptionsLoop = True  

def SearchAccountID():
  PasswordID = input("PassowrdID: ")
  ReadtoCSV = open("Database.csv","r")
  for line in ReadtoCSV:
    if line == PasswordID:
      print("x")
  ReadtoCSV.close()
  
WelcomeMenu()