from pprint import pprint
import random
import sys
import json
# import nltk
from store import *

class MarkovChain:

	def __init__(self, file, n = 3):
		self.memory = {}
		self.n = n
		self.file = file
		self.store = Trigram('database/'+file.split('/')[-1].strip('.txt')+'.db')
		self.ngrams = []
	
	
	def process_file(self):
		with open(self.file, 'r', encoding = "ISO-8859-1") as f:
			for line in f:
				self.ngrams.append(self.learn(line.split()[1:]))
		# print(self.ngrams)
		self.to_store(self.ngrams)
	
	def _learn_key(self, *key, value):
		
		if key not in self.memory:
			self.memory[key] = []

		self.memory[key].append(value)
	
	def to_store(self, ngrams):
		self.store.add_many(ngrams)
	
	def query(self, *words):
		return (self.store.get_ngram_values(*words))
	
	def learn(self, tokens):
		# tokens = text.split(" ")
		
		# ngrams = [(tokens[i], tokens[i + 1], tokens[i + 2]) for i in range(0, len(tokens) - 2)]
		ngrams = [[tokens[i+j] for j in range(self.n)] for i in range(0, len(tokens) - (self.n-1))]
		
		for ngram in ngrams:
			self._learn_key(*ngram[:self.n-1], value = ngram[-1])
		return ngrams[0]
		# pprint(ngrams)
		
	def next(self, *current_state):
		next_possible = self.memory.get(current_state)
		if not next_possible:
			next_possible = self.memory.keys()

		return random.sample(next_possible, 1)

if __name__ == '__main__':
	m = MarkovChain(sys.argv[1], int(sys.argv[2]))
	# m.process_file()
	pprint(m.query('a', 'baby'))
	# pprint(m.memory)
	# print(m.next(*sys.argv[3].split()))
	
	