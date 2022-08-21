import Calender as cld
from datetime import date

class Transaction:
  def __init__(myself, title, type, amount):
    myself.title = title
    myself.type = type
    myself.amount = amount
    myself.date = date.today().strftime("%d/%m/%Y")
    today = date.today()

  def print(self):
    print("Title: "+self.title)
    print("Date: "+self.date)
    print("Type: "+self.type)
    print("Amount: "+str(self.amount))




temp = Transaction("my first transaction","credit",10400)
temp.print()


