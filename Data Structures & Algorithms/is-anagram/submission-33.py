class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1

        for c in t:
            if c in hashmap:
                hashmap[c] -= 1

        return all(v == 0 for v in hashmap.values())
        