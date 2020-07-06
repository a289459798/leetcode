class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        lis = []
        for str in s:
            if str in lis:
                index = lis.index(str)
                lis = lis[index+1:]
                
            lis.append(str)
            length = max(len(lis), length)
        return length


a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))