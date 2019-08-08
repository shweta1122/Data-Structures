mydict = {0: "o' clock", 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen',
          17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine',30: 'half past'}


def words(h,m):
    s =''
    if m<=30:
        if m==15:
            s+= mydict[int(m)] +' '+'past'+' '+ mydict[h]

        elif m==1:
            s += mydict[int(m)]+' '+'minute'+' '+'past'+' '+mydict[h]

        elif m == 30:
            s += mydict[m]+' '+mydict[h]
        elif m==00:
            s+=mydict[h]+' '+mydict[int(m)]

        else:
            s+=mydict[int(m)]+' '+'minutes'+' '+'past'+' '+mydict[h]

    else:
        m=60-m
        if m == 15:
            s += mydict[int(m)] + ' '+'to'+' ' + mydict[h+1]
        elif m == 1:
            s += mydict[int(m)]+' '+'minute'+' '+'to'+' '+mydict[h+1]
        elif m == 30:
            s += mydict[m]+' '+mydict[h]
        elif m == 00:
            s += mydict[h]+' '+mydict[int(m)]

        else:
            s += mydict[int(m)]+' '+'minute'+' '+'to'+' '+mydict[h+1]




    print(s)





h=5
m=59
words(h,m)
