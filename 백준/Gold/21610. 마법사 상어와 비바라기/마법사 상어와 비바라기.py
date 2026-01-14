n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
move = []
for _ in range(m):
    d, s = map(int, input().split())
    move.append((d-1, s))

# 초기 구름 (n은 어차피 2 이상)
cld = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
direct = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

for md, ms in move:
    new_cld = []
    new_arr = [[0]*n for _ in range(n)]
    dx, dy = direct[md]
    dx, dy = dx*ms, dy*ms

    # 모든 구름에 대해
    for cx, cy in cld:
        nx, ny = (cx+dx)%n, (cy+dy)%n
        if nx < 0:
            nx = n+nx
        if ny < 0:
            ny = n+ny
        arr[nx][ny] += 1
        new_arr[nx][ny] = arr[nx][ny]
        new_cld.append((nx, ny))

    # 구름이 모두 사라지고 난 다음에 대각선 4방향 계산해야 한다
    for cld_x, cld_y in new_cld:
        cnt = 0
        for dx2, dy2 in [(-1,-1), (-1,1), (1,1), (1,-1)]:
            if 0<=cld_x+dx2<n and 0<=cld_y+dy2<n and arr[cld_x+dx2][cld_y+dy2] >= 1:
                cnt += 1
        new_arr[cld_x][cld_y] += cnt

    # 현재 구름 있는 곳 제외하고
    new_cld_set = set(new_cld)
    cld = []
    for x in range(n):
        for y in range(n):
            if (x,y) not in new_cld_set and arr[x][y] >= 2:
                cld.append((x,y))
                new_arr[x][y] = (arr[x][y] - 2)
            elif (x,y) not in new_cld_set:
                new_arr[x][y] = arr[x][y]

    arr = new_arr

print(sum(sum(a) for a in arr))