print("Coordinate printer")
f=int(input("Specify the first number:"))
l=int(input("Specify the last number:"))
for x in range(f,l+1):
    for y in range(1,5):
        print(f'({x},{y})')