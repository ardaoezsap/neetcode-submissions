class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False

        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        for j in range(len(s)):
            if t[j] in counts:
                counts[t[j]] -= 1
            else:
                return False

        return all(value == 0 for value in counts.values())
