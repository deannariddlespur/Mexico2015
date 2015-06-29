#Directions
print 'Please input the following information rounded to the highest dollar'

# Input your name
name = raw_input('Please type your name:\n')
# Input your monthly income
income = raw_input('Please type your monthly Income:\n')
# Input the amount of rent
rent = raw_input('Please type your monthly rent payment:\n')
# Input the amount of your Internet bill
net = raw_input('Please type the amount of your internet bill:\n')
# Input the amount of your phone bill
phone = raw_input('Please Input the amount of your phone bill:\n')
# Input the amount of your power bill
power = raw_input('Please Input the amount of your power bill:\n')
# Input the  total amount of insurance bill (life/auto/health)
ins = raw_input('Please Input the amount of your insurance bill:\n')
# Input the total amount of your weekly groceries
food = raw_input('Please Input the amount of your weekly groceries bill:\n')
# multiply weekly groceries by 4
total_food = int(food) * 4.00
# add up all debits
total = int(rent) + int(net) + int(phone) + int(power) + int(ins) + int(total_food)
# subtract the debts from the monthly income
true_total = int(income) - total
# if outcome is less than 1000.00 print " you need to do better"
if true_total < 1000.00:
	print 'you need to do better - your left over balance is {true_total}'.format(true_total=true_total)

# If outcome is more than 1000.00 print " your are doing awesome"
else:
	print 'you are doing awesome - your left over balance is {true_total}'.format(true_total=true_total)



# print outcome of the report

