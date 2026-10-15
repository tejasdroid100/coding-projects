print("Welcome to the Car Game")
print("To start you must type Help")
print("type help to see the commands")
first=input("enter here")
first=first.lower()
while first != "help":
    print("Please enter a valid command to start.")
    first = input("enter here ").lower()
print("Start\nStop\nQuit")
print("Type any of these commands: ")
command=input("enter here")
command=command.lower()
if command=="start":
    print("Car has been started")
elif command=="stop":
    print("Car has been stopped")
elif command=="quit":
    print("You quit the game")
else:
    print("Please enter a valid command")

