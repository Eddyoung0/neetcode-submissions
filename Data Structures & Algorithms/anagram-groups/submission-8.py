class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anadict[key].append(i)
        return list(anadict.values())