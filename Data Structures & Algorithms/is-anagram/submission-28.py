class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return _sort(s) == _sort(t)

def _sort(s: str):
    return "".join(sorted(s)).lower()