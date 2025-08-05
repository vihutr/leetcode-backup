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
    def findLucky(self, arr: List[int]) -> int:
        int_count_mapping = {}
        highest = -1
        for i in arr:
            if i not in int_count_mapping:
                int_count_mapping[i] = 0
            int_count_mapping[i] += 1
        for i in int_count_mapping:
            if int_count_mapping[i] == i and i > highest:
                highest = i
        return highest
# @leet end
