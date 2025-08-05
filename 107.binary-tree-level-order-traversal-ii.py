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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([])

        if root:
            result.append([root.val])
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        curr_level = []
        while queue:
            curr_level_len = len(queue)
            # loop through every node in level
            for i in range(curr_level_len):
                t_node = queue.popleft()
                curr_level.append(t_node.val)
                if t_node.left:
                    queue.append(t_node.left)
                if t_node.right:
                    queue.append(t_node.right)
            # once done
            result.append(curr_level)
            curr_level = []
        result.reverse()
        return result

# @leet end
