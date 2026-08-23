class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Greedy

        goal = len(nums) - 1
        step_count = 0

        while goal != 0:
            new_idx = -1
            for idx in range(goal-1, -1, -1):
                if nums[idx] + idx >= goal:
                    new_idx = idx

            print(new_idx, idx, goal)
            goal = new_idx
            step_count += 1

        return step_count