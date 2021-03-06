from random import choice
from time import sleep

breakfast_menu = {
  'Pancakes': 7.49,
  'French Toast': 7.99,
  'Omlet': 6.99,
  'Country Fried Steak': 10.99
}

breakfast_menu_sides = {
  'Bacon': .99,
  'Sausage': 1.49,
  'Eggs': 1.49,
  'Hash Browns': 1.49,
}

lunch_menu = {
  'Steak': 15.99,
  'Hamburger': 12.99,
  'Pasta': 11.99,
  'Ribs': 13.99
}

lunch_menu_sides = {
  'Fries': .49,
  'Salad': .19,
  'Onion Rings': 1.49,
  'Baked Potato': .99 
}

dinner_menu = {
  'Steak': 20.99,
  'Hamburger': 15.99,
  'Pasta': 16.99,
  'Ribs': 17.49 
}

dinner_menu_sides = {
  'Fries': 1.49,
  'Salad': 1.19,
  'Onion Rings': 1.99,
  'Baked Potato': 1.49 
}

def greeting(time, waiter_name):
  print(f"Thanks for coming in to Bottega Diner! We have the best {time} in town!")
  sleep(1)
  print(f"\nMy name is {waiter_name} and I'll be serving you today.")
  sleep(2)
  name = input(f"\nWhat's your name?")
  sleep(1)
  print(f"\nIt is nice to meet you, {name}! Here is your menu!")
  menu(time)
  sleep(2)
  more_time = (input("\nWould you like more time to order?")).lower()
  if more_time == 'yes':
    sleep(5)
  return name

def random_waiter_name():
  waiter_name = choice(['Sam', 'Martha', 'Rosie', 'Mark'])
  return waiter_name

def menu(time):
  print(f"~Bottega Diner~\n\n--{time.capitalize()} Menu--\n")
  print("---Entrees---")
  if time == 'breakfast':
    for food, price in breakfast_menu.items():
      print(f"{food}: ${price}")
    print("\n---Sides---")
    for food, price in breakfast_menu_sides.items():
      print(f"{food}: ${price}")
  elif time == 'lunch':
    for food, price in lunch_menu.items():
      print(f"{food}: ${price}")
    print("\n---Sides---")
    for food, price in lunch_menu_sides.items():
      print(f"{food}: ${price}")
  else:
    for food, price in dinner_menu.items():
      print(f"{food}: ${price}")
    print("\n---Sides---")
    for food, price in dinner_menu_sides.items():
      print(f"{food}: ${price}")

def time_of_day():
  time = choice(['b', 'l', 'd'])
  if time == 'b':
    return 'breakfast'
  elif time == 'l':
    return 'lunch'
  else:
    return 'dinner'    

def order():
  entree = input("\nWhat can I get for you? Let's start with your entree!")
  side_one = input("And your first side?")
  side_two = input("And your second side?")
  correct = input(f"\nAlright, you want the {entree} with {side_one} and {side_two}?").lower()
  if correct == 'yes':
    print("\nI'll get that order right in for you!")
  else:
    print("\nI'm pretty sure that's what you said and that's what you get...")   

def waitress_comments():
  return

class Chef_Special():
  def __init__():
    return
  def random_entree():
    return
  def random_sides(): 
    return

class Bill():
  def __init__():
    return
  def entree_price():
    return
  def sides_prince():
    return

def main():

main()