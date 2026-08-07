n, m = map(int, input().split())
grid = [int(input()) for _ in range(n)]

# m이 1인 경우가 예외일 것이다
# (s, e) 터져야 하는 폭탄 시작위치와 끝위치를 저장

if m == 1:
    print(0)
else:
    while True:

        s, e = 0, 1
        cnt = 1
        loc = []
        while e < len(grid):
            if grid[s] == grid[e]:
                cnt += 1
                e += 1
            else:
                s = e
                e += 1
                cnt = 1
            if cnt >= m and (s,e) not in loc:
                loc.append((s,e))

        if len(loc) == 0:
            break

        for (s,e) in loc:
            grid[s:e] = [0]*(e-s)

        new_grid = []
        for num in grid:
            if num != 0:
                new_grid.append(num)

        grid = new_grid

    print(len(grid))
    for num in grid:
        print(num)


