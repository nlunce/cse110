import math

name = ''
account_names = []
account_balances = []

print('Enter the names and balances of bank accounts (type: quit when done)')
print()

while name != 'quit':
    name = input('What is the name of this account?: ')
    if name != 'quit':
        account_names.append(name.capitalize())
        balance = float(input('What is the balance?: '))
        account_balances.append(balance)

print()
print('Account Information:')
print()
for i, e in enumerate(zip(account_names, account_balances)):
    print(f'{i + 1}. {e[0]} - ${e[1]: .2f}')
print()


mod = input('Do you want to update an account?(yes/no): ')
while mod != 'yes' and mod != 'no':
    print()
    print('INVALID INPUT')
    print()
    mod = input('Do you want to update an account?(yes/no): ')
   


if mod == 'yes':
    index_select = int(input('What account index do you want to update?: '))
    balance = float(input('What is the new balance?: '))
    account_balances[index_select - 1] = balance
elif mod == 'no':
    print()
    print('Account Information:')
    print()
    for i, e in enumerate(zip(account_names, account_balances)):
        print(f'{i + 1}. {e[0]} - ${e[1]: .2f}')
    print()

print()
print('Account Information:')
print()
for i, e in enumerate(zip(account_names, account_balances)):
    print(f'{i + 1}. {e[0]} - ${e[1]: .2f}')
print()