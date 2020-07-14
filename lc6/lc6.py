class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        i = 0
        j = 0
        index = 0
        arr = [[0 for m in range(len(s))] for n in range(numRows)]
        while index < len(s):
            while i < numRows and index < len(s):
                # print('i', i, j, index)
                arr[i][j] = s[index]
                i += 1
                index += 1
            j += 1
            i = numRows - 1
            while i > 0  and index < len(s):
                i -= 1
                # print('j', i, j, index)
                arr[i][j] = s[index]
                j += 1
                index += 1

            i = 1
            j -= 1
        str = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    continue
                str.append(arr[i][j])
        return ''.join(str)


a = Solution()
print(a.convert("PAYPALISHIRING", 3))