class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def count_palindromes(index, odd = True):
            
            l = index
            r = index

            if not odd:
                r += 1

            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        count = 0
        for idx in range(len(s)):
            count += count_palindromes(idx, True) + count_palindromes(idx, False)

        return count