from __future__ import division
from itertools import izip_longest

#okay this one's gonna be a lil bit of a bitch
# but essentially what its supposed to do
# is you take in these strings in FASTA format 
# of length at most 1 kbp (1000 base pairs)
# and fasta format essentially looks like:
'''    
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''
# and what u do is u look at the GC-content for each strings
# AKA what percent of the string is either G or C
# and u return the string w the highest GC-content
# followed by the actual percentage, within .001 accuracy

f = open("input6.txt", "r")

#takes a file, returns all the lines in a list
def line_read(the_file):
	final = []
	for word in the_file:
		final.append(word)
	return final

#takes a list, returns it as a dict-
#with the first entry as a key and the second as the value, and so on
def dict_maker(l):
	return dict(zip(*[iter(l)]*2)) 

#credits: http://stackoverflow.com/questions/6900955/python-convert-list-to-dictionary

def gc_measure(string):
	a = list(string)
	count = 0
	for letter in a:
		if (letter == "C") or (letter == "G"):
			count += 1
	return count/len(string)

def the_biggest_dict(a_dict):
	greatest = 0
	proper_key = ""
	for key in a_dict:
		if gc_measure(a_dict[key]) > greatest:
			proper_key = key
	return proper_key



g = open("output6.txt", "w")
#g.write(gc_measure("GCAT"))
#f.close()
#g.close()