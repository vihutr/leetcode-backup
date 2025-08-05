# @leet start
class MedianFinder:
    # keep track of the media inherently by keeping two lists of values, lower and greater
    # priority queue that allows for efficeint operations when inserting values and rebalancing the two lists
    # python heapq uses stores smallest element at root by default (to be similar to traditional lists)
    # account for this by using negative values for the lower heap (to get the max when popping)
    # this also means when we rebalance and move a value to the other heap we must negate it
    # we assume the possible worst case of adding then finding the median repeatedly
    # for this case this is a good solution (inserting and sorting immediately as efficiently as possible)
    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        # checking b/n lower and higher everytime adds overhead for larger data (this use case)
        # and does not necesarily tell use which one to push to anyways
        if self.lower and self.higher and num >= self.higher[0]:
            heapq.heappush(self.higher, num)
        else:
            # add to lower heap by default and just rebalance as priority queues will sort by default
            heapq.heappush(self.lower, -num)

        # rebalance as necessary
        # once we have at least 2 values we can simply move our highest value
        # (whether it was the prior value or not)
        # to the higher priority queue
        
        # check if value conflicts with ordering between the two roots of the queues
        if self.lower and self.higher and (-self.lower[0]) > self.higher[0]:
            temp = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, temp)
        # and check the lengths to verify maintaining the size for median calculation
        # then adjusting accordingly
        if len(self.lower) > len(self.higher):
            temp = -heapq.heappop(self.lower)
            heapq.heappush(self.higher, temp)
        elif len(self.higher) > len(self.lower):
            temp = -heapq.heappop(self.higher)
            heapq.heappush(self.lower, temp)

    def findMedian(self) -> float:
        # we return our readily available value based on the larger queue
        if len(self.lower) > len(self.higher):
            return -self.lower[0]
        elif len(self.higher) > len(self.lower):
            return self.higher[0]
        # or if same len return the division
        else:
            return (-self.lower[0] + self.higher[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @leet end
