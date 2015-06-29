get_to_know = list()
first_stuff = raw_input('Please type the first stuff about you \n')
get_to_know.append(first_stuff)
second_stuff = raw_input('Please type the second stuff about you\n')
get_to_know.append(second_stuff)
third_stuff = raw_input('Please type the third stuff about you\n')
get_to_know.append(third_stuff)

print 'The things about you are:'

for stuff in get_to_know:
	print stuff