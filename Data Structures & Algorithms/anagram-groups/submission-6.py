class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for i in strs:
            count = [0] *26
            for c in i:
                count[ord(c)-ord('a')] +=1
            key = tuple(count)
            anagram_dict[key].append(i)
        return list(anagram_dict.values())