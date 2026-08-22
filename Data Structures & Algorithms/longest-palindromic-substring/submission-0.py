class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = -1

        def check_palindrome(index, odd = True):
            l = index
            r = index
            if not odd:
                r += 1

            length = -1

            while r < len(s) and l >= 0 and s[l] == s[r]:
                length = r - l + 1
                l -= 1
                r += 1

            return length, l, r

        for i in range(len(s)):
            
            odd_length, odd_l, odd_r = check_palindrome(i, odd = True)
            if odd_length > length:
                length = odd_length
                l = odd_l + 1
                r = odd_r - 1

            odd_length, odd_l, odd_r = check_palindrome(i, odd = False)
            if odd_length > length:
                print(l, r , odd_l, odd_r, i)
                length = odd_length
                l = odd_l + 1
                r = odd_r - 1

        if l >= 0 and r >= 0:
            print(l, r)
            return s[l : r + 1]
        else:
            return ""
        