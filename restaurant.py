MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

# Defines a constant dict with item names (strings) and
# prices (integers)

def restaurant():
    total = 0
    while True:
        # Keeps asking the user for input, until an explicit
        # “break” from the loop
        order = input('Order: ').strip()
        # Gets the user’s input, and uses
        # str.strip to remove leading and trailing whitespace

        if not order:
            # If “order” is an empty string, trailing whitespace
            # break out of the loop.
            break

        if order in MENU:
            # If “order” is a defined menu item,
            # then get its price and add to total.
            price = MENU[order]
            total += price
            print(f'{order} is {price}, total is {total}')

        else:
            # If “order” is neither empty nor in the dict,
            # then we don’t serve this item.
            print(f'We are fresh out of {order} today')
    print(f'Your total is {total}')


restaurant()
