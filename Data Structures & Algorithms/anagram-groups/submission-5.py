class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26 # [0,0,0,0] [a,b,c,d]

            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1
            
            results[tuple(count)].append(s)

        return list(results.values())
        