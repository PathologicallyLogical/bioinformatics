

#okay so this code what it does is that it takes a (presumable dna) string
#and it changes all the T's to U's because thats how transcription works
#sample in: GATGGAACTTGACTACGTAAATT
#sample out: GAUGGAACUUGACUACGUAAAUU

f = open("rosalind_rna.txt", "r")

def changer(string):
	final = ""
	for letter in list(string):
		if letter == "T":
			final += "U"
		else:
			final += letter
	return final

def file_handler(the_file):
	for word in the_file:
		return changer(word)


g = open("output3.txt", "w")
g.write(file_handler(f))
f.close()
g.close()