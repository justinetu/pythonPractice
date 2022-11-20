# This is car game using a while loop
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            print("Car started...")
        started = True
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''start - to start the car\nstop - to stop the car\nquit- to quit
        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand that")
