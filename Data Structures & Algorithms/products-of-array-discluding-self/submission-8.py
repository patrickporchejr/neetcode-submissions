class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        prefixSum = 1
        suffixSum = 1
        for num in nums:
            prefix.append(prefixSum)
            prefixSum *= num

        for i, num in reversed(list(enumerate(nums))):
            prefix[i] *= suffixSum
            suffixSum *= num
            

        return prefix
        # for num in reversed(nums):
        #     suffix.append(suffixSum)
        #     suffixSum *= num

        # suffix.reverse()

        # return [x * y for x, y in zip(prefix, suffix)]

            
            
            