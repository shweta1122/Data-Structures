def count(s1,s2):
   fin=''
   for i in range(0,len(s1)):
    if s1[i]==s2[i]:
        fin+=s1[i]
    elif s2[i+1]==s1[i] or s1[i+1]==s2[i]:
        fin+=s2[i+1]




s1 = "SHINCHAN"
s2 = "NOHARAAA"
print(count(s1, s2))
