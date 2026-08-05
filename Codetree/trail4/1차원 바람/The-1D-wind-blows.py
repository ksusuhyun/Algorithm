n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# 주의할 것: 
# 행과 열이 다르다! nxn 아님
# 바람이 왼쪽에서 불어오면, right shift / 바람이 오른쪽에서 불어오면 left shift

def shift(r, d):
    if d == 'R':
        temp = a[r][0]
        for i in range(m-1):
            a[r][i] = a[r][i+1]
        a[r][-1] = temp
    else:
        temp = a[r][-1]
        for i in range(m-1, 0, -1):
            a[r][i] = a[r][i-1]
        a[r][0] = temp

def check(row1_idx, row2_idx):
    for i in range(m):
        if a[row1_idx][i] == a[row2_idx][i]:
            return 1
    return 0

for q_i in range(q):
    r, d = winds[q_i]
    r -= 1
    # 바람이 분다, 현재 r은 1부터 시작하므로 실제 인덱싱은 r-1로 진행
    shift(r, d)
    up_r, up_d, down_r, down_d = r, d, r, d
    # 윗방향 전파
    while True:
        if up_r-1<0:
            break
        if check(up_r, up_r-1):
            if up_d == 'L':
                new_up_d = 'R'
            else:
                new_up_d = 'L'
            shift(up_r-1, new_up_d)
            up_r = up_r-1
            up_d = new_up_d
        else:
            break
    # 아랫방향 전파
    while True:
        if down_r+1 >= n:
            break
        if check(down_r, down_r+1):
            if down_d == 'L':
                new_down_d = 'R'
            else:
                new_down_d = 'L'
            shift(down_r+1, new_down_d)
            down_r = down_r+1
            down_d = new_down_d
        else:
            break

for l in a:
    print(*l)