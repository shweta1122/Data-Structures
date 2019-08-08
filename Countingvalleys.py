def countingValleys(s):
    count = 0
    valleys = []
    for i in s:
        if i == 'U':
            count += 1
        else:
            count -= 1

        if count == 0:
            valleys.append(i)
    print(valleys.count('U'))

s = 'UDDDUDUU'
countingValleys(s)
