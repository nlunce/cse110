from operator import sub
from tkinter.messagebox import YES
import math

child_price =  float(input('What is the price of the child\'s meal?: '))
adult_price = float(input('What is the price of the adults\'s meal?: '))
children_number = int(input('How many children are there?: '))
adult_number = int(input('How many adults are there?: '))
sales_tax = float(input('What is the sales tax?: '))
senior_discount = input('Are you over the age of 65?(Yes/No): ')
sales_tax_con = sales_tax/100
subtotal = child_price * children_number + adult_price * adult_number
sales_tax_total = subtotal * sales_tax_con
total = subtotal + sales_tax_total
print()
print()

if senior_discount.lower() == 'yes':
    print('Senior discount of 10% off applied')
    discounted_amount = total * .1
    print('Discounted Amount: $' + format(discounted_amount, '.2f'))
    total = total - discounted_amount
else:
    print('Not applicable for senior discount.')

print('Subtotal: $' + str(format(subtotal, '.2f')))
print('Sales Tax: $' + str(format(sales_tax_total, '.2f')))
print('Total: $' + str(format(total, '.2f')))
payment_amount = float(input('What is the payment amount?: $'))
change = payment_amount - total
print('Change: $' + str(format(change, '.2f')))

