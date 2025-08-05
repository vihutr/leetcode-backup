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
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = False
        consonant = False
        for c in word:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    vowel = True
                else:
                    consonant = True
            elif 48 <= ord(c) <= 57:
                pass
            else:
                return False
        if vowel and consonant:
            return True
        return False
# @leet end
