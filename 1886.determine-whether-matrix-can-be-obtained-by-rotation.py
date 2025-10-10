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


def printl(mat):
    for m in mat:
        print(m)
    print()


def transpose(mat: List[List[int]]):
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


def invert_rows(mat: list[list[int]]):
    for row in range(len(mat)):
        left = 0
        right = len(mat) - 1
        while left < right:
            mat[row][left], mat[row][right] = mat[row][right], mat[row][left]
            left += 1
            right -= 1


def rotate_90_cw(mat):
    transpose(mat)
    invert_rows(mat)


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # there are only 3 possibilities for rotating a matrix
        # simply calculate them and compare
        if target == mat:
            return True
        for i in range(3):
            rotate_90_cw(mat)
            if target == mat:
                return True
        return False
# @leet end

