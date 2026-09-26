class Solution:
    seen = {}
    def climbStairs(self, n: int) -> int:
        if (n <= 3):
            self.seen[n] = n
            return n
        
        if n not in self.seen:
            self.seen[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.seen[n]
        else:
            return self.seen[n]