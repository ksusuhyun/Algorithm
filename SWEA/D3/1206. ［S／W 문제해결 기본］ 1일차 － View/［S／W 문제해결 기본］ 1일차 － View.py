for tc in range(10):
    n = int(input())
    house = list(map(int, input().split()))

    loc = []
    for i in range(len(house)):
        if house[i] != 0:
            loc.append((house[i], i))

    ans = 0
    for l, i in loc:
        new = [house[i-2], house[i-1], house[i+1], house[i+2]]
        if max(new) < l:
            ans += l-max(new)

    print(f'#{tc+1} {ans}')