n, m, q = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
rect = []
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    rect.append([(r1-1,c1-1), (r2-1, c2-1)])

# 직사각형 테두리 배열 반환하는 함수
def rect_out(r1, c1, r2, c2):
    r_out = []
    # 첫번째 테두리
    for i in range(c1, c2):
        r_out.append(grid[r1][i])
    # 두번째 테두리
    for i in range(r1, r2):
        r_out.append(grid[i][c2])
    # 세번째 테두리
    for i in range(c2, c1, -1):
        r_out.append(grid[r2][i])
    # 네번째 테두리
    for i in range(r2, r1, -1):
        r_out.append(grid[i][c1])
    return r_out

def rect_reout(r1, c1, r2, c2, r_out):
    p = 0
    for i in range(c1, c2):
        grid[r1][i] = r_out[p]
        p += 1
    for i in range(r1, r2):
        grid[i][c2] = r_out[p]
        p += 1
    for i in range(c2, c1, -1):
        grid[r2][i] = r_out[p]
        p += 1
    for i in range(r2, r1, -1):
        grid[i][c1] = r_out[p]
        p += 1


def right_shift(arr):
    temp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

for l in rect:
    r1, c1, r2, c2 = l[0][0], l[0][1], l[1][0], l[1][1]
    r_out = rect_out(r1, c1, r2, c2)
    right_shift(r_out)
    rect_reout(r1, c1, r2, c2, r_out)

    # 기본값을 -1로 둘 것
    # grid에 들어올 수 있는 숫자의 범위가 0부터 9이기 때문에
    # 0을 new_grid의 기본값으로 두면 문제가 생길 수 있다
    new_grid = [[-1]*m for _ in range(n)]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            ij_sum = grid[i][j]
            ij_cnt = 1
            for (dx, dy) in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<m:
                    ij_sum += grid[nx][ny]
                    ij_cnt += 1
            new_grid[i][j] = int(ij_sum // ij_cnt)

    for i in range(n):
        for j in range(m):
            if new_grid[i][j] == -1:
                new_grid[i][j] = grid[i][j]

    grid = new_grid

for r in grid:
    print(*r)


