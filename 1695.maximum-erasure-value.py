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
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = end = max_sum = curr_sum = 0
        seen = set()
        for n in nums:
            while n in seen:
                seen.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            seen.add(n)
            curr_sum += n
            end += 1
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
# @leet end
