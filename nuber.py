#Input your name for the receipt
name = raw_input('Please type your name:\n')
#Input the number of miles you traveled
first_number = raw_input('How many miles did you ride with us today?:\n')
#multiplies the number of miles by the current rate per mile
total = int(first_number) * 2.00
#prints the receipt with name and total amount for the current ride
print 'Thank you {name} for your ride with us today'.format(name=name)
print 'The total is {total}'.format(total=total)