class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        data = {}
        for i in range(len(s)):
            if s[i] not in data:
                data[s[i]] = 0
            data[s[i]] += 1
        for i in range(len(t)):
            if t[i] in data:
                data[t[i]] -= 1;
        for k in data:
            if data[k] != 0:
                return False
        return True

Solution().isAnagram('aacc', 'ccac')