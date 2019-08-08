def isBalanced(s):
    l=[]
    flag=0
    for i in s:
        if i=='(' or i=='{' or i=='[':
            l.append(i)
        else:
            if i == ')' or i == '}' or i == ']':
                if len(l)!=0:
                    if i==')' and l[len(l)-1]=='(':
                        l.pop()
                    elif i == '}' and l[len(l)-1] == '{':
                        l.pop()
                    elif i == ']' and l[len(l)-1] == '[':
                        l.pop()
                    else:
                        flag=1
                        break
                else:
                    flag=1
                    break
    if flag==1:
        return 'NO'
    else:
        return 'YES'


t = int(input())

for t_itr in range(t):
    s = input()

    print(isBalanced(s))
