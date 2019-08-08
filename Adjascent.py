# def maxSubsetSum(arr):
#     dp = []
#     dp.append(arr[0])
#     dp.append(max(arr[:2]))
#     ans = max(dp)
#     for a in arr[2:]:
#         dp.append(max(max(dp[-2]+a, a), ans))
#         ans = max(ans, dp[-1])
#     return ans
# arr=[-2,-1,3,-4,5]
# print(maxSubsetSum(arr))

def maxSubsetSum(arr):
    sol=[]
    add=[]
    for i in range(0,len(arr)):
        a=[]
        for j in range(i,len(arr),2):
            a.append(arr[j])
        sol.append(a)
        a=[]

        for k in range(i+2,len(arr)):
            a.append(arr[i])
            a.append(arr[k])
            sol.append(a)
            a=[]
    for i in sol:
        add.append(sum(i))

    return max(add)

def main():
    n = int(input())
    if (n<=10**5 and n>=1):
    
        arr = [int(n) for n in input().split()]
        for i in arr:
            if i>=(-10)**5 and i<=10**5:

                if(len(arr)==n):
                    return (maxSubsetSum(arr))
                else:
                    return 0
    else:
        return 0

print(main())