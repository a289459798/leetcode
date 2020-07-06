def pow(x, y):
    res = 1
    while(y > 0):
        res *= x
        y -= 1
    return res

def pow2(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        tmp = pow2(x, y / 2)
        return tmp * tmp
    else:
        tmp = pow2(x, (y - 1) / 2)
        return tmp * tmp * x

# print(pow(2, 8))
print(pow2(2, 9))


def pow3(x, y) :
    res = 1
    while y > 0:
        res *= x
        y -= 1
    return res

def pow4(x, y):

    if y == 1:
        return x
    elif y % 2 == 0:
        tmp = pow4(x, y /2)
        return tmp * tmp
    else:
        tmp = pow4(x, (y - 1) / 2)
        return tmp * tmp * x