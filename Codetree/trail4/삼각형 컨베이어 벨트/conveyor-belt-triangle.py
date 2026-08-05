n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
def shift(l, r, d):
    new = l+r+d
    temp = new[-1]
    for i in range(3*n-1, 0, -1):
        new[i] = new[i-1]
    new[0] = temp

    return new[0:n], new[n:2*n], new[2*n:]

for _ in range(t):
    l,r,d = shift(l, r, d)

print(*l)
print(*r)
print(*d)