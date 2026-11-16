# 시작점을 주면 가로 체크하는 함수
def check_ga(i,j,n):
    cnt_ga = 0
    while j < n:
        if arr[i][j] == 1:
            visit_ga[i][j] = 1
            cnt_ga += 1
            j += 1
        else:
            break
    return cnt_ga

# 시작점을 주면 세로 체크하는 함수
def check_se(i,j,n):
    cnt_se = 0
    while i < n:
        if arr[i][j] == 1:
            visit_se[i][j] = 1
            cnt_se += 1
            i += 1
        else:
            break
    return cnt_se
            
t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    ans = 0
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    visit_ga = [[0]*n for _ in range(n)]
    visit_se = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 흑이면 pass
            if arr[i][j] == 0:
                pass
            else:
                # 가로, 세로 체크는 독립적으로 이루어져야 한다. if elif 로 묶이면 안된다
                if visit_ga[i][j] == 0:
                    cnt_ga = check_ga(i,j,n)
                    if cnt_ga == k:
                        ans += 1
                if visit_se[i][j] == 0:
                    cnt_se = check_se(i,j,n)
                    if cnt_se == k:
                        ans += 1
               
    print(f'#{tc+1} {ans}')