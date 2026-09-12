class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for item in range(len(freq) - 1, 0, -1):
            for num in freq[item]:
                res.append(num)
                if len(res) == k:
                    return res

        

        

        