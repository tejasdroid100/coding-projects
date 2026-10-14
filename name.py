name=input('Enter your name: ')
length=len(name)
if length<3:
    print("Name is too short")
elif length>3:
    print("Name is good")
elif length>=50:
    print("Name is too long")