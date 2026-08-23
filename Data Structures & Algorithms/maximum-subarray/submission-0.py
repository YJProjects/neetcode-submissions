class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        minimum_total = 0

        res = -float('inf')
        total = 0

        for num in nums:
            total += num
            res = max(res, total - minimum_total)

            minimum_total = min(total, minimum_total)
        
        return res

        #[2,-3,4,-2,2,1,-1,4]

        # 2 -1 3 1
        # 3 1