loot = {}
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        n = len(nums)
        houses1 = nums[:n-1]
        houses2 = nums[1:n]

        #print(houses1, houses2)
        #print(self.rob2(houses2), self.rob2(houses1))

        return max(self.rob2(houses2), self.rob2(houses1))

    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        loot[0] = nums[0]
        loot[1] = max(nums[0],nums[1])

        for i in range(len(nums)):
            if i > 1:
                loot[i] = max(nums[i] + loot[i-2], loot[i-1])

        #print(loot)
        return loot[len(nums)-1]