# A class for trie nodes
class TrieNode:
    # Initializes a trie node
    def __init__(self):
        # Initialize attributes
        self._children = {}
        self._is_word = False
        #self._is_root = False
    

    # adds a word to the Trie (only used during initialization)
    def add_word(self, word):
        self._add_word(word, 0)

    def _add_word(self, word, i):
        if word[i] in self._children:
            if len(word)-1 == i:
                node._is_word = True
            else:
                self._children[word[i]]._add_word(word, i+1)
        else:
            node = TrieNode()
            if len(word)-1 == i:
                node._is_word = True
            else:
                node._add_word(word, i+1)
            self._children[word[i]] = node

        
    # Find the node with a given prefix
    def find_node(self, prefix):
        return self._find_node(prefix, 0)
    def _find_node(self, prefix, i):
        if prefix == '':
            return self
        elif prefix[i] not in self._children:
            return None
        else:
            if i == len(prefix)-1:
                return self._children[prefix[i]]
            else:
                return self._children[prefix[i]]._find_node(prefix, i+1)

    # Generate all the words with the given prefix
    #def get_words(self, prefix): 
        #yield from self._get_words(prefix, 0, prefix)
    # def _get_words(self, prefix, i, str):
    #     if self.is_word:
    #         yield str
    #         if self._children:
    #             for letter in self._children:
    #                 yield from self._children[letter]._get_words(prefix, i, str+letter)

    #     elif i < len(prefix):
    #         yield from self._children[prefix[i]]._get_words(prefix, i + 1, str)
    #     else:
    #         for letter in self._children:
    #             yield from self._children[letter]._get_words(prefix, i, str+letter)
    def get_words(self, prefix):
        if self._is_word:
            yield prefix
            if len(self._children) > 0:
                for letter in self._children:
                    yield from self._children[letter].get_words(prefix+letter)
        else:
            for letter in self._children:
                yield from self._children[letter].get_words(prefix+letter)


    # Return the number of words in the trie
    def get_nb_words(self, prefix = ''):
        count = 0
        if len(prefix) > 1:
            return self.find_node(prefix).get_nb_words()
        if self._is_word:
            child_count = 0
            if len(self._children) > 0:
                for letter in self._children:
                    child_count = child_count + self._children[letter].get_nb_words()
            return 1 + child_count
        else:
            for letter in self._children:
                count = count + self._children[letter].get_nb_words()
        return count
if __name__ == '__main__':
    my_words = ['am', 'at', 'ate', 'eat', 'mat', 'me', 'met', 'tea', 'tee']
    node = TrieNode()
    for word in my_words: node.add_word(word)
    i = 0
    
    for w in node.get_words(''):
        assert(w == my_words[i])
        i += 1
    assert i == len(my_words)
# A class that implements a prefix tree for words
# This is the "public facing" interface - users interact with WordTrie directly
# TrieNode is private. Users do not directly use that class, but WordTrie can.
# Note that this class is defined for you - you do not need to make any changes.
class WordTrie:
    def __init__(self, words):
        self._root = TrieNode()                         # root node is empty
        for word in words: self._root.add_word(word)    # add all words to trie

    # Generate all the words with a given prefix
    def get_words(self, prefix=''):
        node = self._root.find_node(prefix)     # Locate the node corresponding to the given prefix

        if node is not None:                
            yield from node.get_words(prefix)   # Yield from the generator defined for trie nodes

    # Generate all the words in the prefix tree
    def __iter__(self):
        yield from self.get_words() # Yield from the more general generator

    # Return the number of words with a given prefix
    def get_nb_words(self, prefix=''):
        node = self._root.find_node(prefix)                   # Locate the node corresponding to the given prefix
        return node.get_nb_words() if node is not None else 0 # Delegate the work to the node class
        
    # Return the number of words in the prefix tree
    def __len__(self):
        return self._root.get_nb_words()    # Delegate the work to the node class

    # Implement the in operator: Returns True if word is in the prefix tree
    def __contains__(self, word):
        node = self._root.find_node(word)           # Locate the node corresponding to the given prefix            
        return (node is not None) and node._is_word  # Return true if the node exists and is a word

if __name__ == '__main__':
    words = ['ability','able','about','above','accept','according','account','across','act','action','activity','actually','add','address','administration','admit','adult','affect','after','again','against','age','agency','agent','back','bad','bag','ball','bank','bar','base','be','beat','beautiful','because','become','bed','before','begin','behavior','cold','collection','college','color','come','commercial','common','community','company','compare','computer','concern','condition','conference','consider','event','ever','every','everybody','everyone','everything','evidence','exactly','example','executive','exist','expect','experience']
    my_words = ['am', 'at', 'ate', 'eat', 'mat', 'me', 'met', 'tea', 'tee']
    ramm_words = ['rammed', 'rammer', 'rammers', 'ramming']
    my_trie = WordTrie(words)
    i = 0
    for w in my_trie.get_words('ramme'):
        #assert(w == ramm_words[i])
        i += 1
    #print(my_trie.get_nb_words('ramme'))
    for word in my_words:
        assert word+"puff" not in my_trie
    assert 'activity' in my_trie
    assert "activityx" not in my_trie
    assert len(my_trie) == len(words)
# alphabetical?