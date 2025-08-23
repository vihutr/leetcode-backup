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
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        points = 0
        # n is basically the "21", can not exceed
        # k = when a player stops drawing numbers
        # not related to deck of cards, truly random
        # maxPts = upper value limit in our "deck of cards" with true randomness each time
        
        # effectively a stats problem
        # if "brute forcing", likely use dp
# @leet end
