n = int(input())
ans = []
for i in range(1, n+1):
    cnt = 0
    str_i = list(str(i))
    # 33 같은 케이스 주의
    cnt += str_i.count('3')
    cnt += str_i.count('6')
    cnt += str_i.count('9')

    if cnt == 0:
        ans.append(''.join(str_i))
    else:
        ans.append(''.join(['-']*cnt))
        
print(*ans)
