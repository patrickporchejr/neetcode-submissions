class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list) # { [1,0,0,0,1...]: [eat, tea] }

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            results[tuple(count)].append(s)

        return list(results.values())