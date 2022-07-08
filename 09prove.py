import math
import time

print()
print('Welcome to the Shopping Cart Program!')
print()
user_input = ''
shopping_cart = []
shopping_list = []
total = 0.0

while user_input != 6:
    user_input = int(input('Please select one of the following:\n\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Apply Discount\n6. Quit\n\nPlease enter an action: '))
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
        
        if total > 0:
            print()
            print(f'The total price of the items in the shopping cart is: ${total :.2f}')
            print()
        else:
            for i in range(len(shopping_cart)):
                total = total + shopping_cart[i][1]
            print()
            print(f'The total price of the items in the shopping cart is: ${total :.2f}')
            print()
    elif user_input == 5:
        for i in range(len(shopping_cart)):
            total = total + shopping_cart[i][1]
        
        discount_user_input = int(input(f'\nThe total price of the items in the shopping cart is: ${total :.2f}\n\nPlease select the discount you would like to apply:\n\n1. Senior Citizen Discount\n2. Employee Discount\n\nDiscount: '))
        if len(shopping_cart) >= 1:
            if discount_user_input == 1:
                print('Senior citizen discount of 10% off applied')
                total = total - (total * .1)
                print()
                print(f'Total: {total : .2f}')
                time.sleep(1)   
            elif discount_user_input == 2:
                print('Employee discount of 20% off applied')
                total = total - (total * .2)
                print()
                print(f'Total: {total : .2f}')
                time.sleep(1.5)
            else:
                print('INVALID INPUT')
        else:
            print('\nCan not apply discount, shopping cart is empty.\n')
            time.sleep(1.5)


print('Thank you. Goodbye.')

       
        



