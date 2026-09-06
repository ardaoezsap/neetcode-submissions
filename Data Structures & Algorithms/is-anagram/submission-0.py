class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False

        return self.countCreator(s) == self.countCreator(t)

        

    def countCreator(self, s: str) -> dict:
        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        return counts
     
