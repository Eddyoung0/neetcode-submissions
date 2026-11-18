class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gdict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord('a')- ord(i)]+=1
            key = tuple(count)
            gdict[key].append(s)
        
        return list(gdict.values())