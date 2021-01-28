#AtCoder Beginner contest 189 solution
#D-Logical Expression
#Shubham yadav



N = int(input())
T = 1
F = 1
for i in range(N):
  A = input()
  if A == "AND":
    F = T+(2*F) 
  else:
    T = (2*T)+F
print(T)
