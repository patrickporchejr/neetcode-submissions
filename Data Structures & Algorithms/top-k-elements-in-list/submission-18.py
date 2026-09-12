class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # { 1: 1, 2: 2, 3: 3 }
        count = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key, val in hashmap.items():
            count[val].append(key)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)

                if (len(res) == k):
                    return res



        

        

        