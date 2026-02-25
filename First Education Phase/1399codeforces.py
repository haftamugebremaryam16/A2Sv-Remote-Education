t=int(input())
for j in range(t):
    n=int(input())
    notfound=True
    arr=list(map(int,input().split()))
    arr.sort()
    for i in range(1,len(arr)):
        if abs(arr[i]-arr[i-1])>1:
            print("NO")
            notfound=False
            break
    if notfound:
        print("YES")
    
