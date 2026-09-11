class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index 

        for index, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], index]

            hashmap[num] = index
        return []



        