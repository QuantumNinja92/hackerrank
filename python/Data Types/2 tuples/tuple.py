import __builtin__

N = int(raw_input())
vals = (raw_input()).split(" ")
L = []
for i in range(0, N):
    L.append(int(vals[i]))

T = tuple(L)
myHash = hash(T)
print myHash