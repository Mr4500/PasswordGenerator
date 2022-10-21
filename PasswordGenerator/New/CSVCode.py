def AddToCSV(Email,AccountType,Username,Password,PasswordID):
  WritetoCSV = open("Database.csv","a")
  WritetoCSV.write(f"{Email},{AccountType},{Username},{Password},{PasswordID}\n")
  WritetoCSV.close()

def SearchAccountID():
  PasswordID = input("PassowrdID: ")
  ReadtoCSV = open("Database.csv","r")
  for line in ReadtoCSV:
    if line == PasswordID:
      print("x")
  ReadtoCSV.close()