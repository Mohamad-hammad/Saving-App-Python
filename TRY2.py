import Calender
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
    for i in self.allTransactions:
      i.print()
    print("------------------\n\n")

def numToMonth(num):
  datetime_object = datetime.strptime(str(num), "%m")
  full_month_name = datetime_object.strftime("%B")
  return full_month_name


class Year:
  months = []
  def addTransaction(self,transaction):
    transc = Transaction()
    transc = transaction
    x = datetime.strptime(transc.Date,"%d/%m/%Y")
    tranMonth = numToMonth(x.month)
    print(transc.Date)
    print ( x.month)
    print(numToMonth(x.month))
    flag=False
    for i in self.months:
      if i.name == tranMonth:
        i.addTransaction(transaction)
        flag = True

      





temp1 = Transaction()
temp1.addTransaction("transaction#1","credit","meezan",1111,'1/08/2022')
year = Year()
year.addTransaction(temp1)