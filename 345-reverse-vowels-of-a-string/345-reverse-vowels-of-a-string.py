class Solution:
    def reverseVowels(self, s: str) -> str:
        ms = {'a','e','i','o','u','A','E','I','O','U'}
        ans = []
        for i in range(len(s)):
            if s[i] in ms:
                ans.append(s[i])
        news = [char for char in s]
        for i in range(len(s)):
            if s[i] in ms:
                l = len(ans)-1
                news[i] = ans[l]
                ans.pop(l)
        return ''.join(news)
            