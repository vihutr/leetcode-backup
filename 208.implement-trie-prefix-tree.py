# @leet start
class Trie:

    # Good memory usage but likely not intended method of solving
    # Very inefficient
    def __init__(self):
        self.contain = set()

    def insert(self, word: str) -> None:
        self.contain.add(word)

    def search(self, word: str) -> bool:
        return word in self.contain
        
    def startsWith(self, prefix: str) -> bool:
        for w in self.contain:
            if w.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @leet end
