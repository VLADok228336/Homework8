print("Enter 6digit number")
num = input()
num1 = map(int, num)
sum1 = num1[0] + num1[1] + num1[2]
sum2 = num1[3] + num1[4] + num1[5]
if sum2>sum1:
    print(sum2)
else:
    print(sum1)