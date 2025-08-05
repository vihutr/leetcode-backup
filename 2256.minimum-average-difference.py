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
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_dif = float('inf')
        min_i = 0
        left = 0
        right = sum(nums)
        for i, n in enumerate(nums):
            left += n
            left_avg = left // (i + 1)
            right -= n
            if right != 0:
                right_avg = right // max((len(nums) - 1 - i), 1)
            elif right == 0:
                right_avg = 0
            # print(i, n, left, left_avg, right, right_avg)
            avg_dif = abs(right_avg - left_avg)
            # print(avg_dif, min_avg_dif)
            if avg_dif < min_avg_dif:
                min_avg_dif = avg_dif
                min_i = i
        return min_i
# @leet end
