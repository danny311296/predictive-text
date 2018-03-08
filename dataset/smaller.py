import sys

with open(sys.argv[1], 'r') as fin:
	with open(sys.argv[1].strip('.txt')+'small'+'.txt', 'w') as fout:
		for i, line in enumerate(fin):
			if(i == 50):
				break
			print(line, file = fout, end = '')
			