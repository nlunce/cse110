price = float(input('What is the price?: '))

payment = float(input('what is the payment?: '))

if payment > price:
    change = payment- price
    print (f'Your change is {change}')