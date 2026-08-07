n = int(input())
grid = [ list(map(int, input().split())) for _ in range(n) ]
r, c = map(int, input().split())

# 폭탄 위치를 받으면 터뜨리는 함수
def bomb(r, c):
    size = grid[r-1][c-1]

    grid[r-1][c-1] = 0
    for i in range(size):
        for (dx, dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = (r-1)+i*dx, (c-1)+i*dy
            if 0<=nx<n and 0<=ny<n:
                grid[nx][ny] = 0

bomb(r, c)

new_grid = [[0]*n for _ in range(n)]
for c in range(n):
    temp = []
    for r in range(n-1, -1, -1):
        if grid[r][c] != 0:
            temp.append(grid[r][c])
    temp = temp[::-1]
    temp = [0]*(n-len(temp)) + temp
    for new_r in range(n):
        new_grid[new_r][c] = temp[new_r]

for r in new_grid:
    print(*r)