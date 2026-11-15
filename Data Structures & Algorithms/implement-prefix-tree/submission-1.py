class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.childrens:
                curr.childrens[char] = TrieNode()
            curr = curr.childrens[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]
        return True
        
        