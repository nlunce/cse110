from operator import sub

child_price =  float(input('What is the price of the child\'s meal?: '))
adult_price = float(input('What is the price of the adults\'s meal?: '))
children_number = int(input('How many children are there?: '))
adult_number = int(input('How many adults are there?: '))
sales_tax = float(input('What is the sales tax?: '))
sales_tax_con = sales_tax/100
subtotal = child_price * children_number + adult_price * adult_number
sales_tax_total = subtotal * sales_tax_con
total = subtotal + sales_tax_total
print('Subtotal: $' + str(format(subtotal, '.2f')))
print('Sales Tax: $' + str(format(sales_tax_total, '.2f')))
print('Total: $' + str(format(total, '.2f')))
payment_amount = float(input('What is the payment amount?: $'))
change = payment_amount - total
print('Change: $' + str(format(change, '.2f')))

