t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    arr_90 = [[0]*n for _ in range(n)]
    arr_180 = [[0]*n for _ in range(n)]
    arr_270 = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # 90도는 마지막 열부터
            arr_90[j][n-1-i] = str(arr[i][j])
            # 180도는 마지막 행부터 반대로
            arr_180[n-1-i][n-1-j] = str(arr[i][j])
            # 270도는 첫번째 열부터 반대로
            arr_270[n-1-j][i] = str(arr[i][j])
    
    print(f'#{tc+1}')
    for k in range(n):
        print(''.join(arr_90[k]), ''.join(arr_180[k]), ''.join(arr_270[k]))    