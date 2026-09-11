class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = num
            else:
                return True
        
        return False