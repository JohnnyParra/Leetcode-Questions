from typing import List
import math

def findMinDifference(timePoints: List[str]) -> int:
    minutes = []
    for time in timePoints:
      split = time.split(":")
      minutes.append(int(split[0]) * 60 + int(split[1]))

    minutes.sort()
    
    minDiff = float(math.inf)
    for i in range(0, len(minutes) - 1):
      minDiff = min(minDiff, minutes[i + 1] - minutes[i])

    return min(minDiff, (minutes[0] + (1440 - minutes[len(minutes) - 1])))

print(findMinDifference(["23:59","00:00"]))
print(findMinDifference(["12:12","00:13"]))
print(findMinDifference(["00:00","23:59","00:00"]))