class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for item in s:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

        for item in t:
            if item in count:
                count[item] -= 1

        return all(v == 0 for v in count.values())
            


        