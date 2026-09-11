class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a....z 

            for char in s:
                # map a to index 0
                # map z to index 25
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

        