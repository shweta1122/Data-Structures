list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=list(reversed(['y','tor','e','eps','ay',' ','le','n']))
print(" ".join(list(map(lambda x : ''.join(x) ,list(zip(list1,list2))))))
