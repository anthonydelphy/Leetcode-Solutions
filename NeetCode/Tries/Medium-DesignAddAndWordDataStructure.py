class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True
    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            for w in range(i,len(word)):
                if word[w] == '.':
                    for y in curr.children.keys():
                        if dfs(w+1, curr.children[y]):
                            return True
                    return False
                else:
                    if word[w] not in curr.children:
                        return False
                    curr = curr.children[word[w]]
            return curr.endOfWord                         
        return dfs(0, self.root)

        
