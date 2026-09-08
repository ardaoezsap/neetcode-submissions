class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = {}
        
        for i in range(len(strs)):

            sortedString = "".join(sorted(strs[i]))

            if sortedString in anagramDict:
                anagramDict[sortedString].append(strs[i])
            else:
                anagramDict[sortedString] = [strs[i]]
        
        return list(anagramDict.values())
                

