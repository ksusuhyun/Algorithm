t = int(input())
for tc in range(t):
    s = list(input())

    if len(s) % 2 == 0:
        n = len(s) // 2
    else:
        n = len(s) // 2 + 1

    flag = 1
    for i in range(n):
        if s[i] != s[len(s)-1-i]:
            flag = 0
            break

    print(f'#{tc+1} {flag}')