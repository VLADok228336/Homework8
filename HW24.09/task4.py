print("Enter quadrat side", end="")
side = int(input())
print("Enter round radius", end="")
rad = int(input())
if (side**2 + side**2) **0.5 == rad:
    print("Yes")
else:
    print("No")
if side/2 == rad:
    print("Yes")
else:
    print("No")