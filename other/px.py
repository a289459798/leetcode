data = [2, 5, 3, 8, 4, 9]

def maopao():
    for i in range(len(data) - 1):
        hasChange = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                hasChange = True
                data[j], data[j+1] = data[j+1], data[j]
        if hasChange == False:
            break
    return data
def charu():
    for i in range(len(data)):
        for j in range(i-1, 0, -1):
            if data[j] < data[j-1]:
                data[j-1], data[j] = data[j], data[j-1]
            else:
                break
            print(data)
    return data


print(charu())