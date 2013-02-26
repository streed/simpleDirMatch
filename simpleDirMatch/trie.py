
class Trie( object ):

	def __init__( self, words, split=None, join=None ):
		self._num_words = len( words )

		self.root = None
		self.split = split
		self.join = join

		self._make_tree( words )

	def _make_tree( self, words ):
		for w in iter( words ):
			self._insert( w )
	
	def _insert( self, word ):
		if self.root == None:
			self.root = {}

		temp = self.root

		if self.split:
			word = self.split( word )

		for c in word:
			if not c in temp:
				temp[c] = {}
			temp = temp[c]

		if self.join:
			temp["full"] = self.join( word )
		else:
			temp["full"] = word

	def find( self, word ):
		if self.split:
			word = self.split( word )

		temp = self.root
		index = 0
		return self._find_helper( word, 0, temp )
				
	def _find_helper( self, word, index, temp ):
		ret = False
		for k in temp:
			if k == word[index]:
				index += 1

				if index >= len( word ):
					if "full" in temp[k]:
						if self.join:
							ret = temp[k]["full"] == self.join( word )
							break
						else:
							ret = temp[k]["full"] == word
							break
					else:
						index -= 1
				else:
					if ret:
						break
					else:
						ret = self._find_helper( word, index, temp[k] )
		if ret:
			if self.join:
				return self.join( word )
			else:
				return word
		else:
			return False

