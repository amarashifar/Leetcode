class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in result:
                result[temp].append(word)
            else: 
                result[temp] = [word]

        return list(result.values())
