class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for letter in s:
            if letter in char_count:
                char_count[letter] = char_count[letter] + 1
            else:
                char_count[letter] = 1


        for letter in t:
            if letter in char_count:
                char_count[letter] = char_count[letter] - 1

        
        print(char_count)
        return all(val == 0 for val in char_count.values())
        