def pb(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return pb(x - 2) + pb(x - 1)

def pb2(x):
    i = 1
    data = {}
    while i <= x:
        if i == 1:
            data[i] = 1
        elif i == 2:
            data[i] = 1
        else:
            data[i] = data[i - 2] + data[i - 1]
        i += 1
    return data[x]

print(pb(40))