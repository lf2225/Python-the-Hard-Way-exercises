Lexicon_Dict = {'direction': 'north south east west up down left right back'.split(),
				'verb': 'go stop kill eat'.split(),
				'noun': 'door bear princess cabinet'.split(),
				'number': '0 1 2 3 4 5 5 6 7 8 9'.split()}

user_input = raw_input('>   ')
words = user_input.split()

for i in words:
	if i == Lexicon_Dict['direction']:
		print i, 'direction'

	if i == Lexicon_Dict['verb']:
		print i, 'verb'
	
	if i == Lexicon_Dict['noun']:
		print i, 'noun'
	
	if i == Lexicon_Dict['number']:
		print i, 'number'
