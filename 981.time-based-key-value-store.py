# @leet start
class TimeMap:

    def __init__(self):
        # store timestamps and corresponding values as lists of lists
        # list containing lists of timestamp, val
        # sort the list based on timestamp everytime so you can easily get using whatever sorted search algo
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key in self.data:
            # divide and conquer
            values = self.data.get(key, [])
            left = 0
            right = len(self.data[key]) - 1
            # compare mid to timestamp, adjust right/left accordingly
            # trying to find data[key][0] <= timestamp by the closest
            print(f'{left=}{right=}')
            print(f'{timestamp=}')
            while left <= right:
                mid = (left + right) // 2
                print(f'{mid=}')
                print(self.data[key][mid][0])
                if timestamp == self.data[key][mid][0]:
                    return self.data[key][mid][1]
                elif timestamp > self.data[key][mid][0]:
                    left = mid + 1
                    result = self.data[key][mid][1]
                elif timestamp < self.data[key][mid][0]:
                    right = mid - 1
        return result
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end
