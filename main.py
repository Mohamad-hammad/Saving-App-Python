import Calender as cld
class Transaction:
  def __init__(myself, title, type, amount):
    myself.title = title
    myself.type = type
    myself.amount = amount
  def print(self):
    print("Title: "+self.title)
    print("Type: "+self.type)
    print("Amount: "+str(self.amount))
class Month:
  def __init__(myself, month, year):
    myself.month = month
    myself.year = year
    myself.transactions=[]

temp = Transaction("my first transaction","credit",10400)
temp.print()