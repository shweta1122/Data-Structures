
def calc(s):
    alphaDict = dict.fromkeys(s, 0)
    for i in s:
        alphaDict[i] += 1
    
    track={}
    alphaDict2=dict(alphaDict)
    for key,value in alphaDict.items():
        if value not in track:
            track[value]=0
        else:
            track[value]+=1
    freq = (max(track, key=track.get))
    print(freq)
    count=0
    for key,value in alphaDict.items():
        if value==freq and count<2:
            continue
        elif (value-1)==freq and count<2:
            count+=1
        elif count<1:
            count+=1
            alphaDict[key]-=1
            if alphaDict[key]==0:
                del alphaDict2[key]
            else:
                continue
        else:
            return 'NO'
    for value in alphaDict2.values():
        if value==freq:
            return 'YES'
        else:
            return 'NO'


s = "aaaabbcc"
print(calc(s))
