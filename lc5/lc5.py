class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        if len(s) < 2:
            res = s
        else:
            s = '#'.join(list(s))
            maxLen = 0
            index = 0
            for str in s:
                tmp = self.getMax(s, index)
                ss = s[index - tmp / 2 + (tmp + 1) % 2: index + tmp / 2 + 1].replace('#', '')
                if len(ss) > maxLen:
                    res = ss
                    maxLen = len(ss)
                index += 1
        return res

    def getMax(self, s, i):

        left = s[0:i]
        right = s[i+1:len(s) + 1]
        leftLen = len(left)
        rightLen = len(right)
        minLen = min(leftLen, rightLen)
        maxLen = 1
        for j in range(minLen):
            if left[-(j+1)] == right[j]:
                maxLen += 2
            else:
                break

        return maxLen


a = Solution()
print(a.longestPalindrome("abcba"))