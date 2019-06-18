def compute(list1,list2):
    l=[]
    s=""
    for i in range(0,len(list1)):
        if list2[i]==None:
            l=list1[i]
            s=s.__add__(l+" ")
        else:
            l=(list1[i] + list2[i])
            s=s.__add__(l+" ")

    return s
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=list(reversed(['y','tor','e','eps','ay',None,'le','n']))
print(compute(list1,list2))
