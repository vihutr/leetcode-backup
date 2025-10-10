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
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        for spell in spells:
            potion_threshold = math.ceil(success/spell)
            if potions[-1] < potion_threshold:
                pairs.append(0)
                continue
            m = bisect_left(potions, potion_threshold)
            pairs.append(len(potions) - m)

        return pairs


# @leet end
