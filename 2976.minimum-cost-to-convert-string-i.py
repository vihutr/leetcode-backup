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
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # revisit this one
        total_cost = 0
        min_costs = [[float('inf') for _ in range(26)] for _ in range(26)]
        for i in range(len(original)):
            start_c = ord(original[i]) - ord('a')
            end_c = ord(changed[i]) - ord('a')
            min_costs[start_c][end_c] = min(min_costs[start_c][end_c], cost[i])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_costs[i][j] = min(min_costs[i][j], min_costs[i][k] + min_costs[k][j])

        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            source_c = ord(source[i]) - ord('a')
            target_c = ord(target[i]) - ord('a')

            if min_costs[source_c][target_c] == float('inf'):
                return -1
            total_cost += min_costs[source_c][target_c]
        return total_cost

        # for i in range(len(source)):
        #     src = source[i]
        #     tgt = target[i]
        #     for j in range(len(original)):
        #         if original
# @leet end
