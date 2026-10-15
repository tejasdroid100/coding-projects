print("!!!!Welcome to the Car Game!!!!")
print("To start you must type Help")
print("Type 'help' to see the commands")
first=input("enter here: ")
first=first.lower()
while first != "help":
    print("Please enter a valid command to start.")
    first = input("Enter here ").lower()
print("Type These Commands After The '>' sign:\nStart\nStop\nQuit")
while True:
    command = input(">").lower()
    if command=="start":
        print("Car has been started")
        continue
    elif command=="stop":
        print("Car has been stopped")
        continue
    elif command=="quit":
        print("You quit the game")
        break
    else:
        print("Please enter a valid command")

