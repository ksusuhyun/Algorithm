grid = [ list(map(int, input().split())) for _ in range(4) ]
d = input()

# 한 개의 행 또는 열에 해당하는 arr을 줬을 때
# 두 개의 연속된 숫자들이 있으면 이를 더해버리는 함수
def two_sum(arr, d):
    if d == 'R' or d == 'D':
        arr = arr[::-1]
    elif d == 'L' or d == 'U':
        arr = arr

    # 항상 포인터 2개를 쓸 땐, 애초에 input 배열의 길이가 1인 경우를 생각할 것!!
    if len(arr) == 1:
        new_arr = arr
    else:
        new_arr = []
        i = 0
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                new_arr.append(arr[i]+arr[i+1])
                i += 2

                if i == len(arr)-1:
                    new_arr.append(arr[i])
            else:
                if i+1 == len(arr)-1:
                    new_arr.append(arr[i])
                    new_arr.append(arr[i+1])
                else:
                    new_arr.append(arr[i])
                i += 1

    if d == 'R' or d == 'D':
        new_arr = [0]*(4-len(new_arr)) + new_arr[::-1]
    elif d == 'L' or d == 'U':
        new_arr = new_arr + [0]*(4-len(new_arr))

    return new_arr

# 
if d == 'R' or d == 'L':
    for i in range(4):
        temp = []
        for j in range(4):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
        new_arr = two_sum(temp, d)
        grid[i] = new_arr
else:
    for i in range(4):
        temp = []
        for j in range(4):
            if grid[j][i] != 0:
                temp.append(grid[j][i])
        new_arr = two_sum(temp, d)
        for new_j in range(4):
            grid[new_j][i] = new_arr[new_j]
        
for r in grid:
    print(*r)