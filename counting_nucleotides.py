from collections import defaultdict

#ok so this code it literally just
#all its for is taking in a string in a file
#and counting all the letters in it
#it's meant for a dna string but i mean i guess it works for everything lol



f = open("rosalind_dna.txt", "r")
def counter(string):
	d = defaultdict(int)
	for i in list(string):
		d[i] += 1
	return d

def file_handler(the_file):
	for word in the_file:
		return counter(word)

def print_dict(dicts):
	final = ""
	a = sorted(dicts)
	for key in a:
		print dicts[key]
		

b = file_handler(f)
print print_dict(b)
g = open("output2.txt", "w")
g.write("potato")
f.close()
g.close()