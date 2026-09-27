loot = {}

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        loot[0] = nums[0]
        loot[1] = max(nums[0],nums[1])

        for i in range(len(nums)):
            if i > 1:
                loot[i] = max(nums[i] + loot[i-2], loot[i-1])

        print(loot)
        return loot[len(nums)-1]