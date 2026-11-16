def find_nine(i, j):
    nine = []
    for dx in range(3):
        for dy in range(3):
            nine.append(arr[i+dx][j+dy])        
    return nine

t = int(input())
for tc in range(t):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    
    f_ga, f_se, f_nine = 0, 0, 0

    for ga in arr:
        if len(set(ga)) != 9:
            f_ga = 1
            break
    
    for i in range(9):
        se = []
        for j in range(9):
            se.append(arr[j][i])
        if len(set(se)) != 9:
            f_se = 1
            break
        
    for x, y in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
        nine = find_nine(x,y)
        if len(set(nine)) != 9:
            f_nine = 1
            break
    
    if f_ga == 0 and f_se == 0 and f_nine == 0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')
        
    