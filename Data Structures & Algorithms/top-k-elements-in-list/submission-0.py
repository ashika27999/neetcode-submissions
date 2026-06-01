class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for item, value in count.items():
            bucket[value].append(item)


        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res