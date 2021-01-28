#AtCoder Beginner contest 189 solution
#E-Rotate and Flip
#Shubham yadav




import numpy as np
import sys

input = sys.stdin.readline
N = int(input())
x_y_l = [np.array(list(map(int, input().split())) + [1]) for _ in range(N)]

M = int(input())
m_l = [np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])]
op1 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
op2 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
for _ in range(M):
    m = m_l[-1]
    op = input()
    if " " in op:
        op, p = map(int, op.split())
    else:
        op = int(op)
        p = 0
    if op == 1:
        m_l.append(np.dot(op1, m))
    elif op == 2:
        m_l.append(np.dot(op2, m))
    elif op == 3:
        op3 = np.array([[-1, 0, 2 * p], [0, 1, 0], [0, 0, 1]])
        m_l.append(np.dot(op3, m))
    else:
        op4 = np.array([[1, 0, 0], [0, -1, 2 * p], [0, 0, 1]])
        m_l.append(np.dot(op4, m))

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    ans = np.dot(m_l[a], x_y_l[b - 1])
    print(ans[0], ans[1])

