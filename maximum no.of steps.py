def minjumps(arr,1,h):
    if (h==1):
        return 0
    if (arr[1]==0):
        return float('inf')
    min=float('inf')
    for i in range(1+1,h=1):
        if (i<1+arr[1]+1):
            jumps=minjumps(arr,i,h)
            if(jumps!=float('inf')and jumps+1<min):
                min=jumps+1
                return min
            arr=[1,3,6,3,2,3,6,8,9,5]
            n=len(arr)
print('minimum no.of jumps to reach','end is',minjumps(arr,0,n-1))
