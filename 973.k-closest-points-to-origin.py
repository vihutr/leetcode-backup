# @leet start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        for a, b in points:
            results.append((math.sqrt(a**2 + b**2), (a,b)))
        results.sort(key=getFirst)
        output = []
        for i in range(k):
            output.append(results[i][1])
        return output
def getFirst(element):
    return element[0]
# @leet end
