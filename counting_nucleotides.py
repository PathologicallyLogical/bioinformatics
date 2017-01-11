from collections import defaultdict

f = open("name.txt", "w")
f.write("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
f.close()
'''f = open("name.txt", "r")

def counter(the_file):
	d = defaultdict(int)
	for i in list(the_file):
		d[i] += 1
	return d

def print_dict(dicts):
	for key in dicts:
		print str(key) + " " + str(dicts[key]) 

a = str(print_dict(counter(f)))

g = open("output2.txt", "w")
g.write("a")
f.close()
g.close()'''