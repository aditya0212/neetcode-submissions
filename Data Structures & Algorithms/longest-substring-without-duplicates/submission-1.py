class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        if len(s) == 0:
            return 0
        else:
            char = set()
            char.add(s[0])
        
            ans = 1

            i=0
            j=1

            while j<len(s):
                while s[j] in char:
                    char.discard(s[i])
                    i += 1
                char.add(s[j])
                j += 1
                ans = max(ans, (j-i))
            return ans
                