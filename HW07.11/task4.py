s = ""
g= input().split()
for i in g:
    try:
        if int(i) %2 ==0:
            s+=i + " "
    except:
        continue
print(s)