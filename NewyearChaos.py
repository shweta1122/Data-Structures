def calc(l,o):
    count = 0
    temp = 0
    for i in range(1, len(l)):
        key = l[i]

        j = i-1
        while j >= 0 and key < l[j]:
            l[j+1] = l[j]
            temp += 1
            j -= 1
            count += 1
        l[j+1] = key
        temp = 0

    if count<=len(o)-2:
        return count
    else:
        return 'Too chaotic'
    


l = [1,2,5,3,7,8,6,4]
original = []
maximum = max(l)
for i in range(1, maximum+1):
    original.append(i)
print((calc(l, original)))
