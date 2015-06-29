todolist = list()
first_thing = raw_input('Please type the first thing you do\n')
todolist.append(first_thing)
second_thing = raw_input('Please type the second thing you do\n')
todolist.append(second_thing)
third_thing = raw_input('Please type the third thing you do\n')
todolist.append(third_thing)

print 'The things to buy are:'

for thing in todolist:
	print thing