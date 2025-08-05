# @leet start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create map of chars how much of each char appears in t
        # use defaultdict with int to make new values start at 0 by default
        t_map = collections.defaultdict(int)
        for c in t:
            t_map[c] += 1
        # iterate over string in one direction
        # form a separate mapping, only adding when the letter is also a key in t_map
        # when the maps are equal add that as a result
        # then get the substring of that result to only include the 2 most recent relevant chars
        # and subtract from the mapping the trimmed relevant char, and continue
        # keep track of the index of each in a queue?
        # or use a pointer to iterate over as pointing to the left limit of subarray
        # new substr will have its len() subtracted by the diff between the first two of the stack
        s_map = collections.defaultdict(int)
        for key in t_map:
            s_map[key] = 0
        left = -1
        queue = deque([])
        right = 0
        result = ""
        while right < len(s):
            s_map[s[right]] += 1
            queue.append([s[right], right])
            if s_map[s[right]] > t_map[s[right]]:
                s_map[s[right]] -= 1
                # remove first instance found of the char
                for q in queue:
                    if q[0] == s[right]:
                        queue.remove(q)
                        break
            if t_map == s_map:
                # print('identical maps')
                left = queue.popleft()[1]
                substr = s[left:right + 1]
                # print(substr)
                s_map[s[left]] -= 1
                if result == "" or len(substr) < len(result):
                    result = substr


            # print(queue)
            # print(s_map)
            right += 1
        return result

# @leet end
