import heapq

class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.is_end_of_word=False
        self.frequency=0
        self.word=None
        
class AutoComplete:
    def __init__(self) -> None:
        self.root=TrieNode()
    
    def insert(self, word, frequency):
        node=self.root
        for char in word:
            if char not in node.children:
                node[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
        node.frequency=frequency
        node.word=word
    
    def get_prefixes(self, prefix):
        if not prefix:
            return []
        node=self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        heap=[]
        self._collect_suggestion(node=node, heap=heap)
        result=[]
        while heap and len(result)<5:
            freq, word = heapq.heappop(heap)
            result.append(word)
        return word                    

    def _collect_suggestion(self, node, heap):
        if node.is_end_of_word:
            heapq.heappush(heap, (-node.frequency, node.word))
        
        for char in sorted(node.children):
            self._collect_suggestion(node.children[char], heap=heap)