class Transaction:
  def __init__(myself, title, type, amount):
    myself.title = title
    myself.type = type
    myself.amount = amount

class Month:
  def __init__(myself, name, year):
    myself.name = name
    myself.year = year

  def myfunc(abc):
    print("Hello my name is " + abc.name)

