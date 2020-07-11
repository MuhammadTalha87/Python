
car_started = False
while True:
    command = input("Enter the command : ").lower()
    if command == "start":
        if car_started == True:
            print("car is already started. You can not start again")
        else:
            print(" car is started")
            car_started = True

    elif command == "stop":
        if car_started == True:
            print("car is stopped")
            car_started = False
        else:
            print("Car is already stopped")
            
    elif command =="drift":
        if car_started == True:
             print("car is drifting")
        else:
           print("Car is not started yet")
    elif command == "lights":
        if car_started == True:
            print("Lights are turned on")
        else:
          print("Car is not started yet")
    elif command == "help":
        print(""" 
        start: To start the car
        Stop: To stop the car
        Drift: To drift the car 
        lights: To Switch on the lights""")
    elif command == "exit":
        break
    else:
        print("Wrong command ! Please type HELP for commands")