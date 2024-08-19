from machine_data import resources
from machine_data import MENU


def check_resources(user_request, water_balance, milk_balance, coffee_balance, there_are_resources):
  if user_request == "espresso":
    if water_balance < MENU["espresso"]["ingredients"]["water"]:
      print("Sorry there is not enough water.")
      there_are_resources = False
      return there_are_resources
    elif coffee_balance < MENU["espresso"]["ingredients"]["coffee"]:
      print("Sorry there is not enough coffee.")
      there_are_resources = False
      return there_are_resources
  elif user_request == "latte":
    if water_balance < MENU["latte"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        there_are_resources = False
        return there_are_resources
    elif milk_balance < MENU["latte"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        there_are_resources = False
        return there_are_resources
    elif coffee_balance < MENU["latte"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        there_are_resources = False
        return there_are_resources
  elif user_request == "cappuccino":
      if water_balance < MENU["cappuccino"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        there_are_resources = False
        return there_are_resources
      elif milk_balance < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        there_are_resources = False
        return there_are_resources
      elif coffee_balance < MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        there_are_resources = False
        return there_are_resources


def count_coins():
  print("Please insert coins.")
  quarters = float(input("How many quarters?: "))
  dimes = float(input("How many dimes?: "))
  nickles = float(input("How many nickles?: "))
  pennies = float(input("How many pennies?: "))
  total_money = round((quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01), 2)
  return total_money


def process_payment(user_request, machine_balance, user_money):
  if user_request == "espresso":
    if user_money < MENU["espresso"]["cost"]:
      print("Sorry that's not enough money. Money refunded.")
      return machine_balance
    else:
      return machine_balance + MENU["espresso"]["cost"]
  if user_request == "latte":
    if user_money < MENU["latte"]["cost"]:
      print("Sorry that's not enough money. Money refunded.")
      return machine_balance
    else:
      return machine_balance + MENU["latte"]["cost"]
  if user_request == "cappuccino":
    if user_money < MENU["cappuccino"]["cost"]:
      print("Sorry that's not enough money. Money refunded.")
      return machine_balance
    else:
      return machine_balance + MENU["cappuccino"]["cost"]

machine_balance = 0.0
water_balance = resources["water"]
milk_balance = resources["milk"]
coffee_balance = resources["coffee"]
machine_on = True
while machine_on:
  user_request = input("What would you like? (espresso/latte/cappuccino): ")
  if user_request == "off":
    machine_on = False
  elif user_request == "report":
    print(f"Water: {water_balance}ml")
    print(f"Milk: {milk_balance}ml")
    print(f"Coffee: {coffee_balance}ml")
    print(f"Money: ${machine_balance}")
  elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
    there_are_resources = True
    there_are_resources = check_resources(user_request, water_balance, milk_balance, coffee_balance, there_are_resources)
    if not there_are_resources == False:
      user_money = count_coins()
      machine_balance = process_payment(user_request, machine_balance, user_money)
      if user_money > MENU[user_request]["cost"]:
        user_change = round(user_money - MENU[user_request]["cost"], 2)
        print(f"Here is ${user_change} dollars in change.")
      if user_request == "espresso":
        water_balance -= MENU["espresso"]["ingredients"]["water"]
        coffee_balance -= MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso. Enjoy")
      if user_request == "latte":
        water_balance -= MENU["latte"]["ingredients"]["water"]
        milk_balance -= MENU["latte"]["ingredients"]["milk"]
        coffee_balance -= MENU["latte"]["ingredients"]["coffee"]
        print("Here is your latte. Enjoy")
      if user_request == "cappuccino":
        water_balance -= MENU["cappuccino"]["ingredients"]["water"]
        milk_balance -= MENU["cappuccino"]["ingredients"]["milk"]
        coffee_balance -= MENU["cappuccino"]["ingredients"]["coffee"]
        print("Here is your cappuccino. Enjoy")