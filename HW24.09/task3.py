print("How much time is left to lunch?", end=" ")
lunch = int(input())
print("How many details do you must to do?", end="")
howmany = int(input())
print(f"Before lunch you can do {lunch//4} details")
print(f"To finish plan you should work {howmany*4//60} h {howmany*4%60} m")

