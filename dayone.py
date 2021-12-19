# This is a simple program to demonstrate swapping of two vatiables

# Get user input for two variables
#x = input('Enter a value for x: ')
#y = input('Enter a value for y: ')

# x.y = x, y
#z = x
#x = y
#y = z

#print(x + ',' + y)

qty_adult = 0
qty_child = 0
qty_senior = 0

while True:
    ticket_type = input('What kind of ticket you like to buy? (adult, child, serionn- Q to quit) ')
    if ticket_type == "Q":
        break

    if ticket_type == 'adult':
        qty_adult += 1
    elif ticket_type == 'child':
        qty_child += 1
    elif ticket_type == 'senior':
        qty_senior += 1

print('Ticket bought: ')
print('Adult: ' + str(qty_adult))
print('Child: ' + str(qty_child))
print('Serion: ' + str(qty_senior))


# x = [1, 5, 3, 8]
# ==> x
# prints:- [1, 5, 3, 8]
# x[2]
# prints 3
# x[2] = 42
# x prints [1, 5, 42, 8]
# to add a value use a variable.append( )
# 3 * [1,2,3} prints a pattern of numbers
# x.instare()
# x.remove()
# for e in x:
#       result += e
# use can ''' and ''' for a multiple comment



    
