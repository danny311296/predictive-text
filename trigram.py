from pprint import pprint
import random
# import nltk

class MarkovChain:
	
	def __init__(self):
		self.memory = {}

	def _learn_key(self, *key, value):
		if key not in self.memory:
			self.memory[key] = []

		self.memory[key].append(value)

	def learn(self, text):
		tokens = text.split(" ")
		trigrams = [(tokens[i], tokens[i + 1], tokens[i + 2]) for i in range(0, len(tokens) - 2)]
		# pprint(trigrams)
		for trigram in trigrams:
			self._learn_key(trigram[0], trigram[1], value = trigram[2])
	
	def next(self, *current_state):
		next_possible = self.memory.get(current_state)

		if not next_possible:
			next_possible = self.memory.keys()

		return random.sample(next_possible, 1)

if __name__ == '__main__':
	m = MarkovChain()
	m.learn('I am Sam. Sam I am. I do not like green eggs and ham.')
	pprint(m.memory)
	print(m.next('I', 'do'))
	
	