class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = defaultdict(int)
        neig = defaultdict(set)
        for i in prerequisites:
            indegree[i[0]] += 1
            neig[i[1]].add(i[0])
        courses = deque()  
        
        for i in range(numCourses):
            if i not in indegree:
                courses.append(i)
        count = 0 
        while courses:
            cur = courses.popleft()
            count +=1
            for i in neig[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    courses.append(i)
                    
        return count == numCourses
        
