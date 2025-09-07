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
    def numTrees(self, n: int) -> int:
        # init a list of results corresponding to each numTrees result,
        # base case 0 and 1 are 1 so we init to 1 matching size n + 1
        stored_results = [1] * (n + 1)
        # start loop at 2 as 0 and 1 are inherent
        # i = number of nodes n in iteration
        # j = given root for current n nodes iteration calculation
        # calculate possible results based on left and right of root
        # left = root - 1 : we cross check left with stored results
        # (always less than current root in iteration)
        # right = current iter n nodes - root val :
        # i.e given n = 4, with current root 2, 1 nodes to left and 2 nodes to right
        # then we ref the table for how many results in each
        # total is the combination of left and right, which corresponds
        # to the current num_nodes
        # suppose 1->1 left and 3->5 right
        # 5 * 1 because of the 5 possibilities on right, with just 1 on left
        # or 2->2 left and 3->5 right
        # 2 * 5 = 10 because of 2 possibties on left with 5 on right:
        for i in range(2, n + 1):
            total = 0
            for j in range(1, i + 1):
                left = j - 1
                right = i - j
                total += stored_results[left] * stored_results[right]
            stored_results[i] = total
        return stored_results[n]

# @leet end
