import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = math.inf

        for num in nums:
            min_num = min(num, min_num)

        return min_num
        