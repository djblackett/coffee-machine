import sys

class CoffeeMachine:
  def __init__(self, money, water, milk, coffee_beans, disp_cups):
    self.coffee_machine = {"money": money, "water": water, "milk": milk, "coffee_beans": coffee_beans, "disp_cups": disp_cups}
    
  def print_state(self):
    print("The coffee machine has: ")
    print(str(self.coffee_machine["water"]) + " of water")
    print(str(self.coffee_machine["milk"]) + " of milk")
    print(str(self.coffee_machine["coffee_beans"]) + " of coffee beans")
    print(str(self.coffee_machine["disp_cups"]) + " of disposable cups")
    print("$" + str(self.coffee_machine["money"]) + " of money")
      
  def get_action(self):
    while True:
      input1 = input("Write action (buy, fill, take, remaining, exit): ")

      if input1 == "buy":
        self.buy()
      elif input1 == "fill":
        self.fill()
      elif input1 == "take":
        self.take()
      elif input1 == "exit":
        sys.exit(1)
      elif input1 == "remaining":
        self.print_state()
    return  
    
    
  def take(self):
    string = "I gave you $" + str(self.coffee_machine["money"])
    print(string)
    self.coffee_machine["money"] = 0
    
  def fill(self):
    water = int(input("Write how many ml of water do you want to add: "))
    milk = int(input("Write how many ml of milk do you want to add: "))
    coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    disp_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    
    if water < 0 or milk < 0 or coffee_beans < 0 or disp_cups < 0:
        print("Enter positive numbers only")
        return
    
    self.coffee_machine["water"] += water
    self.coffee_machine["milk"] += milk
    self.coffee_machine["coffee_beans"] += coffee_beans
    self.coffee_machine["disp_cups"] += disp_cups
    
    return
    
    
    
  def buy(self):
    drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if drink == "1":
      if self.coffee_machine["water"] >= 250 and self.coffee_machine["coffee_beans"] >= 16 and self.coffee_machine["disp_cups"] > 0:
        self.coffee_machine["water"] -= 250
        self.coffee_machine["milk"] += 0
        self.coffee_machine["coffee_beans"] -= 16
        self.coffee_machine["disp_cups"] -= 1
        self.coffee_machine["money"] += 4
        print("I have enough resources, making you a coffee!")
      elif self.coffee_machine[water] < 250:
        print("Sorry, not enough water.")
      elif self.coffee_machine["coffee_beans"] < 16:
        print("Sorry, not enough coffee beans.")
      elif self.coffee_machine["disp_cups"] < 1:
        print("Sorry, not enough disposable cups")
        
    elif drink == "2":
      if self.coffee_machine["water"] >= 350 and self.coffee_machine["milk"] >= 75 and self.coffee_machine["coffee_beans"] >= 20 and self.coffee_machine["disp_cups"] >= 1:
        self.coffee_machine["water"] -= 350
        self.coffee_machine["milk"] -= 75
        self.coffee_machine["coffee_beans"] -= 20
        self.coffee_machine["disp_cups"] -= 1
        self.coffee_machine["money"] += 7
        print("I have enough resources, making you a coffee!")
      elif self.coffee_machine["water"] < 350:
        print("Sorry, not enough water")
      elif self.coffee_machine["milk"] < 75:
        print("Sorry, not enough milk")
      elif self.coffee_machine["coffee_beans"] < 20:
        print("Sorry, not enough coffee beans")
      elif self.coffee_machine["disp_cups"] < 1:
        print("Sorry, not enough disposable cups")
    
    elif drink == "3":
      if self.coffee_machine["water"] >= 200 and self.coffee_machine["milk"] >= 100 and self.coffee_machine["coffee_beans"] >= 12 and self.coffee_machine["disp_cups"] >= 1:
        self.coffee_machine["water"] -= 200
        self.coffee_machine["milk"] -= 100
        self.coffee_machine["coffee_beans"] -= 12
        self.coffee_machine["disp_cups"] -= 1
        self.coffee_machine["money"] += 6
        print("I have enough resources, making you a coffee!")
      elif self.coffee_machine["water"] < 200:
        print("Sorry, not enough water")
      elif self.coffee_machine["milk"] < 100:
        print("Sorry, not enough milk")
      elif self.coffee_machine["coffee_beans"] < 12:
        print("Sorry, not enough coffee beans")
      elif self.coffee_machine[disp_cups] < 1:
        print("Sorry, not enough disposable cups")
      
    elif drink == "back":
      return self.get_action()
    
    return

coffee = CoffeeMachine(550, 400, 540, 120, 9)
#coffee_machine = {"money": 550, "water": 400, "milk": 540, "coffee_beans": 120, "disp_cups": 9}
coffee.get_action()
