class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sort(s) == sort(t)

def sort(s: str):
    return "".join(sorted(s)).lower()