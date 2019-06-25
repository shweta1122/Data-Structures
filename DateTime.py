from itertools import permutations
def months(s):
    month = []
    test_list = perm(s)
    print((test_list))
    for i in test_list:
        if i >= 0 and i <= 12:
            month.append(i)
    try:
        month = max(month)
        return month
    except:
        return 0

def days(s, months):
    day = []
    try:
        for i in months:
            s.remove(i)
        test_list = perm(s)
        for i in test_list:
            if i >= 0 and i <= 31:
                day.append(i)
        
        day = max(day)
        return day
    except:
        return 0

def hours(s, days):
    hour = []
    for i in days:
        if i in s:
            s.remove(i)
        else:
            continue

    test_list = perm(s)
    for i in test_list:
        if i >= 0 and i <= 24:
            hour.append(i)
    try:
        hour = max(hour)
        return hour

    except:
        return 0


def seconds(s,hour):
    second = []
    for i in hour:
        if i in s:
            s.remove(i)
        else:
            continue
    test_list = perm(s)
    for i in test_list:
        if i >= 0 and i <= 60:
            second.append(i)
    try:
        second = max(second)
        return second
    except:
        return 0


def perm(s):
    a = list(permutations(s, 2))

    data = [[str(x) for x in tup] for tup in a]
    data = list(map(lambda x: ''.join(x), data))
    print(data)
    test_list = (list(map(int, data)))
    return test_list


def main():
    s = [0,0,1,2,2,2,3,5,9,9,9,9]
    monthss = months(s)
    a = [int(d) for d in str(monthss)]
    dayss = days(s, a)
    print(s)
    b = [int(d) for d in str(dayss)]
    hourss = hours(s, b)
    c= [int(d) for d in str(dayss)]
    secondss = seconds(s,c)
    if (monthss==0 or dayss ==0 or hourss==0 or secondss==0):
        retn=0
        return retn
    else:
        retn = str(monthss)+'/'+str(dayss) + ' ' + str(hourss)+':'+str(secondss)
        return retn
print(main())
