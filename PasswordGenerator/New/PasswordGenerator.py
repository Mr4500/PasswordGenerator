#imports
import random as random
from random_word import RandomWords

#Naming The Imports
RWG = RandomWords()
RNG = random

def GeneratePassword():
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

def PasswordIDGenerator():
    PasswordID = random.randint(100000, 999999)
    PasswordID = (f"#{PasswordID}")
    print(f"Your Passord ID is: {PasswordID}")