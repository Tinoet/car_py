command = ""
started = False
while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("car is already started...")
    else:
        started = True
        print("car started....")
  elif command == "stop":
    if not started:
        print("car is alreadyy stopped....")
    else:
      started = False
      print("car stopped")
  elif command == "help":
    print("""
    start - to start car
    stop - to stop car
    quit - to exit
    """)
  elif command == "quit":
    break
  else:
    print("sorry, i dont understand....")