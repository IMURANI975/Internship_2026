

def add(expences):
   expense_input = {}
   expense_input["name"] = input("Please input the name: ")
   expense_input["amount"] = input("Please input the amount: ")

   if expense_input["name"] == "" or expense_input["amount"] == "":
      print("Invalid input")
      return

   expences.append(expense_input)
   print("Saved!!!")
   print("Expenses added successfully")


def View(expences):
   for expence in expences:
      print(f"Name: {expence.get('name', '')} | Amount: {expence.get('amount', '')}")
     



expences = []


is_running = True
while is_running:
    print("--------- Expense Tracker Program ---------")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Quit")
    choice = input("Input your choice: ") 
    match choice:
        case "1":
         add(expences)
        case "2":
         View(expences)
        case "3":
          is_running = False
        case _:
          print("Invalid input")
          
