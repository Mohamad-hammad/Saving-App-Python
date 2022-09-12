import Calender as cld
from datetime import date
from datetime import datetime
import pandas as pd
class Transaction:
  title = None
  type = None
  amount = None
  Date = None
  app = None

  def addTransaction(myself, title, type, app, amount,Date=None):
    myself.title = title
    myself.type = type
    myself.amount = amount
    if Date!=None:
      myself.Date = Date
    else:
      myself.Date = date.today().strftime("%d/%m/%Y")
    myself.app = app

  def print(self):
    print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("Title: "+self.title)
    print("Date: "+self.Date)
    print("Type: "+self.type)
    print("App: " + self.app)
    print("Amount: "+str(self.amount))
    print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n")

class Month:
  allTransactions = []
  name = None
  def addDescription(self,name):
    self.name = name
  def addTransaction(myself, title, type, app, amount,Date=None):
    print("adding transaction")
    temp = Transaction()
    temp.addTransaction(title, type, app, amount, Date)
    myself.allTransactions.append(temp)
    myself.allTransactions.sort(key=lambda x: datetime.strptime(x.Date, "%d/%m/%Y"), reverse=True)
  def printAllTransactions(self):
    print("Month : "+self.name)
    for i in allTransactions:
      i.print()
    print("------------------\n\n")
#testing classes
allTransactions = []
temp1 = Transaction()
temp1.addTransaction("transaction#1","credit","meezan",1111,'1/08/2022')

temp2 = Transaction()
temp2.addTransaction("transaction#2","credit","meezan",2222,'2/08/2022')

temp3 = Transaction()
temp3.addTransaction("transaction#3","credit","meezan",3333,'3/08/2022')

temp4 = Transaction()
temp4.addTransaction("transaction#4","credit","meezan",4444)

allTransactions.append(temp1)
allTransactions.append(temp2)
allTransactions.append(temp3)
allTransactions.append(temp4)
#allTransactions.append(temp3)
#allTransactions.append(temp2)
#allTransactions.append(temp1)


temp1.print()
temp2.print()
temp3.print()
temp4.print()

print("before sorting : ")
for i in allTransactions:
  i.print()
print("------------------\n\n")


print("after sorting : ")
allTransactions.sort(key=lambda x: datetime.strptime(x.Date, "%d/%m/%Y"),reverse=True)
#allTransactions.sort(key=lambda x: x.Date, reverse=True)
for i in allTransactions:
  i.print()
print("------------------\n\n")


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n>>>>>>>>>>>>>>>>>>>>>>>>>>>\nTesting month\n\n\n\n")

mymonth = Month()
mymonth.addDescription("may")
mymonth.addTransaction("transaction#1","credit","meezan",1111,'1/08/2022')
mymonth.addTransaction("transaction#2","credit","meezan",2222,'2/08/2022')
mymonth.addTransaction("transaction#3","credit","meezan",3333,'3/08/2022')
mymonth.addTransaction("transaction#4","credit","meezan",4444)

mymonth.printAllTransactions()