#AtCoder beginner contest 189 solutions.
#C-Mandarin orange
#Shubham yadav


N=int(input())
A=list(map(int,input().split()))
ans=0
for i in range(N):
    a=A[i]
    j=0
    l=0
    count=0
    while j<N:
        if a>A[j]:
            count=max(count,l)
            l=0
            j+=1
            continue
        l+=1
        j+=1
    count=max(count,l)
    num=a*count
    ans=max(ans,num)
print(ans)
