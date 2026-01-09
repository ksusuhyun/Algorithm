from collections import deque

n, l, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# bfs 함수 안에서 연합 여러 개를 한 번에 찾는 게 아니라
# 전체를 돌면서 연합을 하나씩 찾고 하나씩 처리하는 방식

def bfs(sx, sy):

    q = deque()

    q.append((sx,sy))
    visited[sx][sy] = 1
    c_list = [(sx,sy)]
    c_sum = arr[sx][sy]

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and l<=abs(arr[nx][ny]-arr[cx][cy])<=r:
                q.append((nx,ny))
                visited[nx][ny] = 1
                c_list.append((nx,ny))
                c_sum += arr[nx][ny]
    
    if len(c_list) > 1: # 연합이 있다
        for x, y in c_list:
            arr[x][y] = c_sum//len(c_list)
        return 1
    return 0

ans = 0
while True:

    flag = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                flag = max(flag, bfs(i,j))
    
    if flag == 0:
        print(ans)
        break
    ans += 1
            