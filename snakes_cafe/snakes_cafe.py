Drinks = ['Coffee', 'Tea', 'Unicorn Tears']
Desserts = ['Ice Cream', 'Cake', 'Pie']
Entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
Appetizers = ['Wings', 'Cookies', 'Spring Rolls']

print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
\n\n
''')
print('Appetizers\n  -------- ')
for i in Appetizers:
    print(' ',i)
print('\n Entrees \n --------  ')
for i in Entrees:
    print(' ',i)
print('\n Desserts \n --------  ')
for i in Desserts:
    print(' ',i)

print('\n Drinks \n -------- ')
for i in Drinks:
    print(' ',i)
print('\n \n ')
print('***********************************')
orderCount = 0
x = []
order = input(
    '\n ** What would you like to order? **  \n \n *********************************** \n \n > ')
x.append(order)


def ordering(order, orderCount):
    while order:
        if order != 'quit':
            print(
                '\n', '**', f'{orderCount+1} order of {order} have been added to your meal', '**')
            order = input(' \n > ')
            x.append(order)
            orderCount += 1

        else:
            break


if __name__ == "__main__":
    ordering(order, orderCount)
    print('\n \n ***********************************  \n\n ** Your  Order List ** \n\n *********************************** ')
    for i in x:
        if i != 'quit':
            print('  ', f'{i}')
    print("\nThank you for visiting our restaurants  <3 \n ")
