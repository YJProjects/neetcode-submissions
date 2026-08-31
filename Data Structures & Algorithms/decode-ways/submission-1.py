class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {}

        def is_valid(s):
            if len(s) == 1 and 1 <= int(s) <= 9:
                return True
            if len(s) == 2 and 10 <= int(s) <= 26:
                return True
            return False

        def recurse(index):
            
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            if index in cache:
                return cache[index]

            one_len = s[index]
            cache[index] = 0

            if is_valid(one_len):
                cache[index] += recurse(index + 1)
            
            
            if index < len(s) - 1:
                two_len = s[index: index + 2]
                if is_valid(two_len):
                    cache[index] += recurse(index + 2)

            return cache[index]

        return recurse(0)
            


            

            

        