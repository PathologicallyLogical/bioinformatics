def sequencer (n, k):
	start = 1
	sec = 1
	if n == 1 or n == 2:
		return start
	new = sequencer(n-2, k) * 3 + sequencer(n-1,k)
	return new



		
print sequencer(5, 3)
print sequencer(28, 3)