class Solution:
    def reverseWords(self, s: str) -> str:
        myWords = s.split(' ')
        ans = []
        for word in myWords:
            wordList = list(word)
            reversedWordList = reversed(wordList)
            finalWord = "".join(reversedWordList)
            ans.append(finalWord)
        return " ".join(ans)