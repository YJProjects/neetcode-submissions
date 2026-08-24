class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)

        if target % 2 != 0:
            return False

        def helper(index, length, total):
            if index >= len(nums):
                return False
            if total == target / 2:
                print(index, length, total)
                return True

            
            result = False

            for i in range(index + 1, len(nums)):
                result = result or (helper(i, length + 1, total + nums[index]) or
                            helper(i, length, total))

            return result

        return helper(0, 0, 0)
            

        