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
    def numSubmat(self, mat: List[List[int]]) -> int:
        numRect = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                num = mat[row][col]
                if num == 1:
                    numRect += 1
                    dimension = 1
                    stillRect = True
                    while stillRect:
                        for i in range(dimension, 0, -1):
                            if mat[row+i]

# @leet end
