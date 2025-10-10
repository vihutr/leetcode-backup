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
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = float('-inf')
        # reverse traversal direction
        # considering k, we will loop form the last k elements
        # this way we touch every element possible, and check fof
        # the max energy at every point
        for i in range(len(energy) - 1, len(energy) - k - 1, -1):
            start_energy = 0
            for j in range(i, -1, -k):
                start_energy += energy[j]
                if start_energy > max_energy:
                    max_energy = start_energy
        return max_energy


# @leet end
