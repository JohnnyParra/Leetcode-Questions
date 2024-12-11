from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
  if sum(gas) < sum(cost):
    return -1

  tank = 0
  start = 0

  for i in range(len(gas)):
    tank += gas[i] - cost[i]
    if tank < 0:
      tank = 0
      start = i + 1
  return start

print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))