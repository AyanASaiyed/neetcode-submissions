class Solution:
    stepCost = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.stepCost[0] = cost[0]
        self.stepCost[1] = cost[1]

        for i in range(len(cost)):
            if i > 1:
                self.stepCost[i] = min(cost[i] + self.stepCost[i-1], cost[i] + self.stepCost[i-2])
            if (i + 1 == len(cost)):
                return min(self.stepCost[i], self.stepCost[i-1])
        
        return self.stepCost[len(cost)-1]

        