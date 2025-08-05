# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        result = 0
        day = 0
        index = 0
        min_heap_for_end_days = []
        # heap needs to fully process after getting all events
        while index < len(events) or min_heap_for_end_days:
            # assign day if empty buffer
            if not min_heap_for_end_days:
                day = events[index][0]
            while index < len(events) and events[index][0] == day:
                heapq.heappush(min_heap_for_end_days, events[index][1])
                index += 1
            print(min_heap_for_end_days)
            heapq.heappop(min_heap_for_end_days)
            day += 1
            result += 1
            while min_heap_for_end_days and min_heap_for_end_days[0] < day:
                heapq.heappop(min_heap_for_end_days)

        return result
# @leet end
