class Solution:
    def compress(self, chars: List[str]) -> int:

        idx = 0
        mod = 0
        res = 0

        # [A 1 B 2 B C D]
        # res = 2
        # idx = 2 count = 2
        # mod =  3

        # A 3 

        while idx < len(chars):
            count = 1

            while idx + 1 < len(chars) and chars[idx] == chars[idx + 1]:
                count += 1
                idx += 1

            chars[mod] = chars[idx]
            mod += 1
            res += 1

            if count > 1:
                count_list = list(str(count))
                for c in count_list:
                    chars[mod] = c
                    res += 1
                    mod += 1

            idx += 1

        return res
            