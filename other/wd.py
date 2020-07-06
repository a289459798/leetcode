T = [23, 25, 21, 19, 22, 26, 23]
def wd1():
    for k, t in enumerate(T):
        for k2, t2 in enumerate(T[k+1:]):
            print(123)
            if t2 > t:
                print(k2 + 1)
                break
# wd1()   # O(n2)

def wd2():
    # 结果集
    res = [0 for _ in range(len(T))]
    print(res)
    stack = []
    for k, v in enumerate(T):
        # 遍历堆栈
        while stack and v > T[stack[-1]]:
            print(123)
            res[stack[-1]] = k - stack[-1]
            stack.pop()
        
        stack.append(k)
    return res

print(wd2())