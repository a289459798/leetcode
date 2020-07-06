class Solution(object):
    def findLength(self, A, B):
        max = []    # 保存最长值
        tmp = []    # 找到相同值临时保存
        start = 0   # B列表的遍历指针位置
        for k, a in enumerate(A):
            for k2, b in enumerate(B[start:]):
                print(a, b)
                if a == b:
                    # 找到相同值
                    tmp.append(a)   # 存到临时变量中
                    start += k2 + 1 # 更新
                    print(tmp)
                else:
                    start = 0
                    if len(tmp) > len(max):
                        max = tmp
                    tmp = []
            start = 0
        if len(tmp) > len(max):
            max = tmp
        return len(max)

print(Solution().findLength([1,2,3,2,1], [3,2,3,2,1]))
