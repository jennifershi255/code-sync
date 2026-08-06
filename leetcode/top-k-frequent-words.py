class Word(object):

    def __init__(self, word):
        self.word = word
    
    def __lt__(self, other):
        return self.word > other.word

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = defaultdict(int)

        for w in words:
            freq[w] += 1
        
        heap = [] # max heap, always stores the k most freq words

        for key,val in freq.items():
            word = Word(key)
            heapq.heappush(heap, (val, word)) # word is the tie breaker

            if len(heap) > k:
                heapq.heappop(heap) # pops least freq. but, in a tie, it pops lowest lexigraphical. we need it to remove the highest lexigraphical first

        res = []

        while heap:
            count, word = heapq.heappop(heap)
            res.append(word.word)
        
        res.reverse() 
        return res