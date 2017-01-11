
f = open("rosalind_revc.txt", "r")

#ok so this one just takes in a dna string and returns 
#the reverse complement

def reverse_complement(string):
	a = list(string)
	final = ""
	for letter in a:
		if letter == "A":
			final = "T" + final
		elif letter == "C":
			final = "G" + final
		elif letter == "G":
			final = "C" + final
		elif letter == "T":
			final = "A" + final
	return final

def file_handler(the_file, funct):
	for word in the_file:
		return funct(word)


g = open("output4.txt", "w")
g.write(file_handler(f, reverse_complement))
f.close()
g.close()