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
    def maximum69Number (self, num: int) -> int:
        # Problem boils down to adding 3
        # to the leftmost 6 digit
        # copy num to gradually iterate over mathematically
        n = num
        place = 1
        to_add = 0

        while n > 0:
            d = n % 10
            if d == 6:
                to_add = 3 * place  # difference between 9 and 6
            n //= 10
            place *= 10

        return num + to_add

        # original soln
        # str_num = str(num)
        # for i in range(len(str_num)):
        #     if str_num[i] == '6':
        #         return int(str_num[:i] + '9' + str_num[i+1:])
        # return num

# @leet end
