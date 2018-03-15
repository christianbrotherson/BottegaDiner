import random

breakfast_menu = {
  'Pancakes': 7.49,
  'French Toast': 7.99,
  'Omlet': 6.99,
  'Country Fried Steak': 10.9
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
  'Salad': .20,
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
  'Salad': 1.20,
  'Onion Rings': 1.99,
  'Baked Potato': 1.49 
}

def menu():
  print("~Bottega Diner~\n\n--Breakfast Menu/Lunch Menu/Dinner Menu--\n")
  print("---Entrees---")
  print("\n-Breakfast Menu-")
  for f, p in breakfast_menu.items():
    print(f"{f}: ${p}")
  print("\n-Breakfast Menu Sides-")
  for f, p in breakfast_menu_sides.items():
    print(f"{f}: ${p}")
  print("\n-Lunch Menu-")
  for f, p in lunch_menu.items():
    print(f"{f}: ${p}")
  print("\n-Lunch Menu Sides-")
  for f, p in lunch_menu_sides.items():
    print(f"{f}: ${p}")
  print("\n-Dinner Menu-")
  for f, p in dinner_menu.items():
    print(f"{f}: ${p}")
  print("\n-Dinner Menu Sides-")
  for f, p in dinner_menu_sides.items():
    print(f"{f}: ${p}")

def time_of_day():
  time = choice(['b', 'l', 'd'])
  if time == 'b':
    return 'breakfast'
  elif time == 'l':
    return 'lunch'
  else:
    return 'dinner'

def waitress_comments():
  return
def order():
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
  print(menu())

main()