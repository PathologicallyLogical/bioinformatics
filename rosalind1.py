f = open('input.txt', 'r')

x = 1

def every_other(the_file):
	final = ""
	index = 1
	for line in the_file:
		if index % 2 == 0:
			final += line
		index += 1
	return final

g = open('output.txt', 'w')
g.write(every_other(f))
f.close()
g.close()