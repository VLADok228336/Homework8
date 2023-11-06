from random import*
kuyituhjgs9zisd = [None]*5
kuyituhjgs9zisd[0] = int(input())
kuyituhjgs9zisd[1] = int(input())
kuyituhjgs9zisd[2] = int(input())
kuyituhjgs9zisd[3] = int(input())
kuyituhjgs9zisd[4] = int(input())

liyujahjg = []
for i in range(10):
    liyujahjg.append(randint(1, 9))
for i in range(5):
    print(kuyituhjgs9zisd[i])
for i in liyujahjg:
    print(i)
r = sum(kuyituhjgs9zisd)
print(r)
umn = 1
for i in liyujahjg:
    umn*=i
ef = ""
print(umn)
if r>umn:
    ef = ">"
if r<umn:
    ef = "<"
if r==umn:
    ef = "="
print(f"First number {ef} second number")
kuyituhjgs9zisd.append(int(input()))
print(kuyituhjgs9zisd)
liyujahjg[int(input())] = int(input())
print(liyujahjg)
print(kuyituhjgs9zisd[4])
kuyituhjgs9zisd.remove(kuyituhjgs9zisd[2])
kuyituhjgs9zisd.remove(kuyituhjgs9zisd[4])
print(kuyituhjgs9zisd)
for i in liyujahjg:
    if i==4 or i ==5:
        liyujahjg.remove(i)
print(liyujahjg)