class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = {}

        for index, word in enumerate(wordsDict):
            if word in self.words:
                self.words[word].append(index)
            else:
                self.words[word] = [index]

    def shortest(self, word1: str, word2: str) -> int:
        
        i = 0
        j = 0

        diff = float('inf')

        # 5
        # 

        while i < len(self.words[word1]) and j < len(self.words[word2]):
            new_diff = abs(self.words[word1][i] - self.words[word2][j])

            diff = min(new_diff, diff)

            if diff == 0:
                return diff

            if self.words[word1][i] < self.words[word2][j]:
                i += 1
            else:
                j += 1

        print(self.words)
        return diff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
