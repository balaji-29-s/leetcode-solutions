class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        totalgas=0
        totalcost=0
        currgas=0
        for i in range(len(gas)):
            totalgas+=gas[i]
            totalcost+=cost[i]
            currgas+=gas[i]-cost[i]
            if currgas<0:
                currgas=0
                start=i+1
        return -1 if totalgas<totalcost else start