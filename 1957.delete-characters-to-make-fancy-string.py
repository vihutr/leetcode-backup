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
    def makeFancyString(self, s: str) -> str:
        ans = []
        for c in s:
            # Check if adding 'c' would create 'ccc'
            if len(ans) >= 2 and ans[-1] == c and ans[-2] == c:
                continue  # Skip adding 'c'
            else:
                ans.append(c)
        return "".join(ans)
        rep_count = 0
        result = prior_char = s[0]
        i = 1
        while i < len(s):
            if prior_char == s[i]:
                rep_count += 1
            else:
                rep_count = 0
            prior_char = s[i]
            if rep_count < 2:
                result += prior_char
            i += 1
        return result


# @leet end
