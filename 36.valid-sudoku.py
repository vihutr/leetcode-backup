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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        sqrs = [[False] * 9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                # skip if empty
                if val == '.':
                    continue
                # convert to int for index checking
                val = int(val) - 1
                # calc index for square/grid
                sqr_i = ((col//3) * 3) + (row//3)

                if rows[row][val] or cols[col][val] or sqrs[sqr_i][val]:
                    return False

                rows[row][val] = True
                cols[col][val] = True
                sqrs[sqr_i][val] = True

        return True


# @leet end
