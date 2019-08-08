def convert(time):
    hr = int(time.split(':')[0])
    if hr == 12:
        if 'AM' in time:
            return '00' + time[2:-2]
        return time[:-2]
    if 'PM' in time:
        hr = str(int(time.split(':')[0])+12)
        return hr+time[2:-2]
    return time[:-2]


# s='07:05:45PM'
print(convert('12:05:45PM'))
print(convert('12:05:45AM'))
print(convert('07:05:45PM'))
