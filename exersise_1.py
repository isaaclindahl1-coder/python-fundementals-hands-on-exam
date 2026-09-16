name = input("What is your first name: ").strip().capitalize()
snack = input("What snack are you getting: ").strip().title()
price = float(input(f"What is the price of the {snack}: "))
quantity = int(input(f"How many {snack} are you getting: "))
total =  price * quantity
if total >= 10:
     discount = total * .90
     print(f"customer: {name}")
     print(f"snack: {snack}")
     print(f"quantity: {quantity}")
     print(f"subtotal: {total: .2f}")
     print(f"discount: {discount: .2f}")
     print(f"Final total: {total * .90: .2f}")
else:
     discount = 0.00
     print(f"customer: {name}")
     print(f"snack: {snack}")
     print(f"quantity: {quantity}")
     print(f"subtotal: {total: .2f}")
     print(f"discount: {discount: .2f}")
     print(f"Final total: {total * .90: .2f}")