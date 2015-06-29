wish_list = list()
first_element = raw_input('Please type your first thing\n')
wish_list.append(first_element)
second_element = raw_input('Please type another thing\n')
wish_list.append(second_element)
third_element = raw_input('Please type your last thing\n')
wish_list.append(third_element)

print 'The elements to buy are:'

for element in wish_list:
	print element
	
