import math
print()
print('Welcome to the Shopping Cart Program!')
print()
user_input = ''
shopping_cart = []
shopping_list = []
total = 0.0

while user_input != 5:
    user_input = int(input('Please select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: '))
    if user_input == 1:

        item = input('What item would you like to add?: ').capitalize()
        price = float(input(f'What is the price of \'{item}\'?: '))

        item_with_price = [item, price]
        shopping_cart.append(item_with_price)
    elif user_input == 2:
        print()
        print('The contents of the shopping cart are: ')
        print()
        for i in range(len(shopping_cart)):
            shopping_list.append([(f'{shopping_cart[i][0]} - ${shopping_cart[i][1]:.2f}')])
            print(f'{i + 1}. '+''.join(shopping_list[i]))
        print()
    elif user_input == 3:
        print()
        print('The contents of the shopping cart are: ')
        print()
        for i in range(len(shopping_cart)):
            print(f'{i + 1}. '+''.join(shopping_list[i]))
        print()

        remove = int(input('Which item would you like to remove?: '))
        print()
        if remove - 1 <= len(shopping_list):
            shopping_list.pop(remove - 1)
            shopping_cart.pop(remove - 1)
        else:
            print('INVALID ITEM')
    elif user_input == 4:
        for i in range(len(shopping_cart)):
            total = total + shopping_cart[i][1]
        print()
        print(f'The total price of the items in the shopping cart is: ${total :.2f}')
        print()

       
        



