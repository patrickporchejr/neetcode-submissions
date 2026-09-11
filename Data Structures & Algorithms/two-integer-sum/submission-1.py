class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracking = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in tracking:
                return [tracking[diff], index]
            tracking[num] = index

        
        