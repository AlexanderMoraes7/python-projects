import random

def bubble(list = []):
    isBigger = True
    while isBigger:
        isBigger = False
        for i in range(len(list)):
            if i == len(list) -1:       # If is the end of list jump to begin
                continue
            if list[i] > list[i + 1]:   # If the value is bigger than later values the change is executed
                isBigger = True
                list[i], list[i + 1] = list[i + 1], list[i]
    return list

num = [random.randrange(0,100) for i in range(10)]

print("Numbers before sort: ", num)
print("Numbers  after sort: ",bubble(num))