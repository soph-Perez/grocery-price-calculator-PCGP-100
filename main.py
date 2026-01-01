def display_items(grocery):
  print(f"\n{'Items'} {'Prices':>20}") 
  for item, price in grocery.items():
    print(f"{item:>6} {price:>20}")

def item_select(grocery): #split this into separate helper functions
  shopping_cart = {}

  while True:
    try:
      item_count = int(input("\nEnter the number of different grocery items: "))
      if item_count <=0:
        raise ValueError
      break
    except ValueError:
      print("\nQuantity must be greater than zero. Try again")

  for i in range(item_count):
    while True:
      try:
        item = input("\nEnter grocery item: ")

        if item not in grocery:
          raise ValueError("not in grocery")

        if item in shopping_cart:
          raise ValueError("already selected")

        break

      except ValueError:
        print("\nInvalid item or item already selected.")

    while True:
      try:
        quantity = int(input("\nEnter the quantity: "))
        if quantity <= 0:
          raise ValueError
        break
      except ValueError:
        print("\nQuantity must be greater than zero.")

    shopping_cart[item] = quantity
  
  return shopping_cart

def calculate_total(cart, grocery):
  total = 0

  for item, quantity in cart.items():
    price = grocery[item]
    total += price*quantity

  return total

def display_summary(cart, grocery, total):
  print(f"\n{'Purchase Summary'}") 
  print(f"\n{'Items'} {'Quantity':>20} {'Price':>20}") 

  for item, quantity in cart.items():
    price = grocery[item]
    print(f"{item:>6} {quantity:>18} {f'${price:.2f}':>22}")
  
  print(f"\nTotal cost: ${total:.2f}")

def main():
  grocery ={
    "apple": 0.75,
    "banana": 0.50,
    "bread": 2.25,
    "milk": 3.00,
    "eggs": 2.50
    }

  display_items(grocery)
  cart = item_select(grocery)
  total = calculate_total(cart, grocery)
  display_summary(cart, grocery, total)
  
if __name__ == "__main__":
    main()