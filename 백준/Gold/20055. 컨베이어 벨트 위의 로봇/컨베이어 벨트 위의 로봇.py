n, k = map(int, input().split())
arr = list(map(int, input().split())) # 내구도 배열

ro = [0]*2*n # 로봇 배열

ans = 0
while True:
    # 회전 하기
    arr = [arr[-1]]+arr[:-1]
    ro = [ro[-1]]+ro[:-1]
    ans += 1

    # 내리는 위치 확인하기
    if ro[n-1] == 1:
        ro[n-1] = 0

    # 먼저 벨트에 올라간 로봇부터!!! for문 돌 때 거꾸로 돌아야 한다
    # 로봇 이동시키기
    for j in range(n-2, 0, -1):
        if ro[j] == 1:
            move_j = (j+1)%(2*n)
            if ro[move_j] != 1 and arr[move_j] >= 1:
                ro[j] = 0
                ro[move_j] = 1
                arr[move_j] -= 1

    # 내리는 위치 확인
    if ro[n-1] == 1:
        ro[n-1] = 0
    # 올리는 위치 확인
    if arr[0] >= 1:
        ro[0] = 1
        arr[0] -= 1
    
    # 내구도 검사
    if arr.count(0) >= k:
        break

print(ans)