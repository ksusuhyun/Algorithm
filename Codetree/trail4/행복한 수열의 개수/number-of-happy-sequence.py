n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 리스트를 줬을 때 행복한 수열인지 확인하는 함수
# "연속"해서 m개 이상의 동일한 원소가 나오는 순간이 존재
def happy(num_list):

    s, e = 0, 1 
    max_len = 0
    while e < n:
        if num_list[s] == num_list[e]:
            e += 1
        else:
            max_len = max(max_len, e-s)
            s = e
            e += 1
    max_len = max(max_len, e - s)

    if max_len >= m:
        return 1
    return 0


# col grid 만들기
col_grid = []
for i in range(n):
    col = []
    for j in range(n):
        col.append(grid[j][i])
    col_grid.append(col)


res = 0
for r in grid:
    if happy(r):
        res += 1

for c in col_grid:
    if happy(c):
        res += 1

print(res)
