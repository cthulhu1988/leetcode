class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        windowSize = 3
        l = len(grid)
        travel = l - windowSize
        count = 0
        maxLocal = [ [0]* (l - 2) for j in range((l - 2))]
        while count <= travel:
            for x in range(0, travel+1):
                maxLoc = self.calculate(x, grid, count)
                maxLocal[x][count] = maxLoc
            count+=1
        return maxLocal
                
    def calculate(self, num, grid, count):
        maxLoc = 0
        windowSize = 3
        for ii in range (num, windowSize + num):
            for jj in range(count, windowSize + count):
                    if grid[ii][jj] > maxLoc:
                        maxLoc = grid[ii][jj]
        return maxLoc
            
