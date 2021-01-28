#AtCoder Beginner contest 189 solution
#F-Sugoroku2
#Shubham yadav



N, M, K = map(int, input().split())
bad = [False] * (N+1)
for x in map(int, input().split()): bad[x] = True
A = [0] * (N+M)
B = [0] * (N+M)
Asum = 0
Bsum = 0
for i in range(N-1, -1, -1):
    if (bad[i]):
        A[i] = 1
        B[i] = 0
    else:
        A[i] = Asum / M
        B[i] = (Bsum / M) + 1
    Asum -= A[i+M]
    Bsum -= B[i+M]
    Asum += A[i]
    Bsum += B[i]
if A[0] > 1 - 1 / (10 ** 10):print(-1)
else: print("%.6f" % (B[0] / (1 - A[0])))
