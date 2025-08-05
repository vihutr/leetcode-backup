# @leet start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq is a list of stacks
        # form a graph of courses
        # checking for if a cycle exists essentially within this graph
        # numCourses is a given, we know how many courses there are.
        
        # cases:
        # multiple pre-reqs for a single course (OK)
        # a single course is pre-req for all other courses (OK)
        # a course is a pre-req for another course that is a pre-req of a the first course (bad)
        
        # must dfs through preqreqs for cycle possibilty:
        # use a queue and have a list of checked nodes

        course_prereq_lookup = {}
        for i in range(numCourses):
            course_prereq_lookup[i] = []

        for p in prerequisites:
            course, prereq = p
            # print(course, prereq)
            if prereq in course_prereq_lookup[course]:
                continue
            if course == prereq:
                return False
            nodes_to_check = deque([])
            nodes_to_check.extend(course_prereq_lookup[prereq])
            nodes_checked = []
            # print('nodes to check: ')
            # print(nodes_to_check)
            while len(nodes_to_check) > 0:
                n = nodes_to_check.popleft()
                # print('nodes to check: ')
                # print(nodes_to_check)
                # print(f'course: {course}')
                # print(f'prereqs compared to: {course_prereq_lookup[n]}')
                # print(f'n: {n}')
                if course in course_prereq_lookup[n] or course == n:
                    # print('cycle detected')
                    return False
                else:
                    nodes_checked.append(n)
                    for m in course_prereq_lookup[n]:
                        if m not in nodes_to_check and m not in nodes_checked:
                            nodes_to_check.append(m)
            course_prereq_lookup[course].append(prereq)
            # print(course_prereq_lookup)
        return True
        
# @leet end
