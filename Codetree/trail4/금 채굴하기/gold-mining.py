n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def get_gold(i,j,k):
    # 마름모 모양은 맨하튼 거리를 따른다
    cnt = 0
    for r in range(-1*k, k+1):
        for c in range(-1*k, k+1):
            if abs(r) + abs(c) <= k and 0<=i+r<n and 0<=j+c<n:
                cnt += grid[i+r][j+c]
    return cnt

# 일단 금이 있는지 확인
is_gold = 0
for l in grid:
    if 1 in l:
        is_gold = 1
        break
        
if is_gold:
    res = []
    # k가 0인 경우를 초기값으로 설정
    cost = 1
    cnt_gold = 1
    gain = (m*cnt_gold) - cost
    res.append((cost, cnt_gold, gain))

    for i in range(n):
        for j in range(n):
            # k가 1부터 n-1인 경우를 본다
            for k in range(1, n+1):
                cost = k**2 + (k+1)**2
                cnt_gold = get_gold(i,j,k)
                gain = (m*cnt_gold) - cost
                if gain >= 0:
                    res.append((cost, cnt_gold, gain))

    # lambda를 활용한 정렬
    res = sorted(res, key=lambda x:-x[1])
    print(res[0][1])
else:
    print(0)





