def calc(s):
    st=""
    count=len(s)
    for i in range(0,len(s)-1):
        st+=s[i]
        st+=s[i+1]
        if(st==s[::-1]):
            count+=1
        elif(st+=s[i+2] == st[::-1]):
            st+=s[i+1]
            if(st == s[::-1]):
                count += 1
        else:
            st=""
        
        
       

        
    return count


s = 'abcbaba'
print(calc(s))



