class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        inputs = [(x.count('0'), x.count('1')) for x in strs]
        cache = {}

        print(inputs)

        def helper(index, M, N):
            if M > m or N > n:
                return -float('inf')
            if index == len(inputs):
                return 0
            if (index, M, N) in cache:
                return cache[(index, M, N)]

            path_skip = helper(index + 1, M, N)
            path_include = 1 + helper(index + 1, M + inputs[index][0], N + inputs[index][1])

            #cache[(index, M, N)] = 
            cache[(index, M, N)] = max(path_include, path_skip)
            return cache[(index, M, N)]

        return helper(0, 0, 0)
            

            