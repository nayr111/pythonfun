drinks = ['Coke', 'Sprite', 'Fanta', 'Coffee', 'Tea', 'Water']

print('Welcome to McDonalds! What would you like to order today?')
order = input('Please enter your order: ')
if order in ['Chicken Nuggets', 'Fries', 'Big Mac', 'McChicken', 'Happy Meal']:
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