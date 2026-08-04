n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def check(i,j):
    if 0<=i<n and 0<=j<m:
        return 1
    return 0

block = [[(0,0), (1,0), (1,1)],[(0,0), (0,1), (1,0)],[(0,0), (0,1), (1,1)],[(1,0), (0,1), (1,1)],[(0,0), (0,1), (0,2)],[(0,0), (1,0), (2,0)]]
def block_sum(i,j):
    now_max= 0
    # b = [], 블록 하나
    for b in block: 
        bs = 0
        for (dx, dy) in b:
            if check(i+dx, j+dy):
                bs += grid[i+dx][j+dy]
            else:
                bs = 0
                break
        now_max = max(now_max, bs)

    return now_max

# 완전탐색
res = 0
for i in range(n):
    for j in range(m):
        now_max = block_sum(i,j)
        res = max(res, now_max)

print(res)