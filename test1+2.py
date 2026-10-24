drinks = ['Coke', 'Sprite', 'Fanta', 'Coffee', 'Tea', 'Water']

print('Welcome to McDonalds! What would you like to order today?')
order = input('Please enter your order: ')
if order == 'Chicken Nuggets':
    n = int(input('How many nuggets would you like to order? '))
    m = int(input('How many boxes of nuggets would you like to order? '))
    def chicken_nuggets(n, m):
        if n <= 0 and m <= 0:
            return "Please order a positive number of nuggets and indicate how many boxes of nuggets you would like to order."
        if n > 100 and m > 10: 
            return "We apologize, but we cannot fulfill orders of more than 100 nuggets and more than 10 boxes."
        elif n <= 0:
            return "Please order a positive number of nuggets."
        elif n > 100:
            return "We apologize, but we cannot fulfill orders of more than 100 nuggets."
        elif m <= 0:
            return "Please indicate how many boxes of nuggets you would like to order."
        elif m > 10:
            return "We apologize, but we cannot fulfill orders of more than 10 boxes."
        else:
            total_nuggets = n * m
            return f'You have ordered {total_nuggets} nuggets in total.'
    print(chicken_nuggets(n, m))
elif order in ['Fries', 'Big Mac', 'McChicken', 'Happy Meal']:
    drink = str(input('Would you like to add a drink to your order?'))
    if drink == 'Yes':
        print('What type of drink would you like?')
        drink_type = str(input('Please enter your drink choice: '))
        if drink_type in drinks:
            print(f'Thank you for your order! You have ordered {order} with a {drink_type}. Your order is being prepared.')
        else:
            print('Invalid drink choice. Please try again.')
    elif drink == 'No':
        print(f'Thank you for your order! You have ordered {order} without a drink. Your order is being prepared.')
    else:
        print('Please input "Yes" or "No" for the drink option.')
else:
    print('Invalid order. Please try again. Perhaps you misspelled your order or it is not on the menu. Please check the menu and try again.')