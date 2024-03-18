# f = open('26_936.txt')
# n, s = map(int,f.readline().split())
# a = [int(x) for x in f]
n, s = map(int,input().split())
a = [140, 150, 160, 200, 220, 240]
a.sort(reverse=1)

k = 0
weight = 0
b = []

while len(a) > 0:
    for i in range(len(a)):
        if sum(b) + a[i] > s:
            b = []
            k += 1
            break
    else:
        b += [a.pop(i)]

print(k)




