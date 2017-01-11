from collections import defaultdict


f = open("rosalind_ini6.txt", "r")

def diction (the_file):
	d = defaultdict(int)
	for line in f:
		for word in line.split(' '):
			d[word] += 1
	return d

def print_dict(dicts):
	for key in dicts:
		print str(key) + " " + str(dicts[key]) 

a = str(print_dict(diction(f)))

g = open("output1.txt", "w")
g.write(a)
f.close()
g.close()
