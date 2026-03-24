import sys
from collections import deque

input = sys.stdin.readline

MAX = 501

visited = [0] * MAX
parent = [-1] * MAX
digit = [''] * MAX

t = int(input())
test_id = 1

for _ in range(t):
    n = int(input())
    
    q = deque()
    
    start = 9 % n
    q.append(start)
    
    visited[start] = test_id
    parent[start] = -1
    digit[start] = '9'
    
    while True:
        cur = q.popleft()
        
        if cur == 0:
            break
        
        nxt = (cur * 10) % n
        if visited[nxt] != test_id:
            visited[nxt] = test_id
            parent[nxt] = cur
            digit[nxt] = '0'
            q.append(nxt)
        
        nxt = (cur * 10 + 9) % n
        if visited[nxt] != test_id:
            visited[nxt] = test_id
            parent[nxt] = cur
            digit[nxt] = '9'
            q.append(nxt)
    
    # tiklash
    res = []
    cur = 0
    while cur != -1:
        res.append(digit[cur])
        cur = parent[cur]
    
    print(''.join(res[::-1]))
    
    test_id += 1