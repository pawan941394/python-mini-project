from pprint import pprint
import random
import time

print("Hii everyone please enter your names here".center(50))
nameString = "Player first Name --> "
name1 = input("first Player Name --> ".center(50))

name2 = input("Second Player Name (if you want to play with computer then type 'c' ) --> ".center(50))
name1list = []
name2list = []
gameMatrix1 = ["", "", ""]
gameMatrix2 = ["", "", ""]
gameMatrix3 = ["", "", ""]
DrwaCheck = 0
computer_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
j=0
def printMatrix():
    for i in gameMatrix1:
        print(f" |  {i}  | ".center(10), end='')
    print()
    print()
    for i in gameMatrix2:
        print(f" |  {i}  | ".center(10), end='')
    print()
    print()
    for i in gameMatrix3:
        print(f" |  {i}  | ".center(10), end='')
    print()
    print()


while True:
    try:
      user1Choice = int(input(f"{name1} please enter your choice number here ( not allow string aur any char and special character) --> ".center(50)))
    except  Exception as e:
        print(f"Please enter a Integer number not a string aur any char and special character".center(50))
        user1Choice = int(input(f"{name1} please enter again your choice number here ( not allow string aur any char and special character) --> ".center(50)))

    if user1Choice > 9:
        pprint("WARNING".rjust(50))
        user1Choice = int(input(f"{name1} please enter right position  --> ".center(50)))

    for item in name1list:
        if user1Choice == item or user1Choice > 9:
            pprint("WARNING".rjust(50))
            user1Choice = int(input(f"{name1} please enter right position  --> ".center(50)))


    for item in name2list:
        if user1Choice == item or user1Choice > 9:
            pprint("WARNING".rjust(50))
            user1Choice = int(input(f"{name1} please enter right p+osition  --> ".center(50)))

    computer_inputs.remove(str(user1Choice))
    name1list.append(user1Choice)
    j = j + 1

    if user1Choice == 1:
        gameMatrix1[0] = "*"

    if user1Choice == 2:
        gameMatrix1[1] = "*"

    if user1Choice == 3:
        gameMatrix1[2] = "*"

    if user1Choice == 4:
        gameMatrix2[0] = "*"

    if user1Choice == 5:
        gameMatrix2[1] = "*"

    if user1Choice == 6:
        gameMatrix2[2] = "*"

    if user1Choice == 7:
        gameMatrix3[0] = "*"

    if user1Choice == 8:
        gameMatrix3[1] = "*"
    if user1Choice == 9:
        gameMatrix3[2] = "*"

    printMatrix()
    if ((gameMatrix1[0] == "*" and gameMatrix1[1] == "*" and gameMatrix1[2] == "*") or (
            gameMatrix2[0] == "*" and gameMatrix2[1] == "*" and gameMatrix2[2] == "*") or (
            gameMatrix3[0] == "*" and gameMatrix3[1] == "*" and gameMatrix3[2] == "*")):
        DrwaCheck = 1
        print(f"Congrats {name1} you won the match")
        printMatrix()
        break

    if ((gameMatrix1[0] == "*" and gameMatrix2[0] == "*" and gameMatrix3[0] == "*") or (
            gameMatrix1[1] == "*" and gameMatrix2[1] == "*" and gameMatrix3[1] == "*") or (
            gameMatrix1[2] == "*" and gameMatrix2[2] == "*" and gameMatrix3[2] == "*")):
        DrwaCheck = 1
        print(f"Congrats {name1} you won the match")
        printMatrix()
        break

    if ((gameMatrix1[0] == "*" and gameMatrix2[1] == "*" and gameMatrix3[2] == "*")):
        DrwaCheck = 1
        print(f"Congrats {name1} you won the match")
        printMatrix()
        break

    if ((gameMatrix1[2] == "*" and gameMatrix2[1] == "*" and gameMatrix3[0] == "*")):
        DrwaCheck = 1
        print(f"Congrats {name1} you won the match")
        printMatrix()
        break
    if ((gameMatrix1[1] == "*" and gameMatrix2[1] == "*" and gameMatrix3[1] == "*")):
        DrwaCheck = 1
        print(f"Congrats {name1} you won the match")
        printMatrix()
        break



    if j == 9:
        print("This match was draw !! Thanks for playing".rjust(50))
        break


    if name2=='c':
        user2Choice = int(random.choice(computer_inputs))
        print(f"computer is thinking............".center(50))
        time.sleep(3)
        print(user2Choice)

    else:

        try:
            user1Choice = int(input(f"{name2} please enter your choice number here ( not allow string aur any char and special character) --> ".center(50)))
        except  Exception as e:
            print(f"Please enter a Integer number not a string aur any char and special character".center(50))
            user2Choice = int(input(f"{name2} please enter again your choice number here ( not allow string aur any char and special character) --> ".center(50)))
        if user2Choice > 9:
          pprint("WARNING".rjust(50))
          user2Choice = int(input(f"{name1} please enter right position  --> ".center(50)))

        for item in name1list:
           if user2Choice == item or user2Choice > 9:
             pprint("WARNING".rjust(50))
             user2Choice = int(input(f"{name1} please enter right position --> ".center(50)))


        for item in name2list:
           if user2Choice == item or user2Choice > 9:

             pprint("WARNING".rjust(50))
             user2Choice = int(input(f"{name1} please enter right position  --> ".center(50)))


    computer_inputs.remove(str(user2Choice))

    name2list.append(user2Choice)
    j = j + 1

    if DrwaCheck == 0 and j == 9:
        print("This match was draw !! Thanks for playing".center(50))
        break

    if user2Choice == 1:
        gameMatrix1[0] = "0"

    if user2Choice == 2:
        gameMatrix1[1] = "0"

    if user2Choice == 3:
        gameMatrix1[2] = "0"

    if user2Choice == 4:
        gameMatrix2[0] = "0"

    if user2Choice == 5:
        gameMatrix2[1] = "0"

    if user2Choice == 6:
        gameMatrix2[2] = "0"

    if user2Choice == 7:
        gameMatrix3[0] = "0"

    if user2Choice == 8:
        gameMatrix3[1] = "0"
    if user2Choice == 9:
        gameMatrix3[2] = "0"
    printMatrix()

    if ((gameMatrix1[0] == "0" and gameMatrix1[1] == "0" and gameMatrix1[2] == "0") or (
            gameMatrix2[0] == "0" and gameMatrix2[1] == "0" and gameMatrix2[2] == "0") or (
            gameMatrix3[0] == "0" and gameMatrix3[1] == "0" and gameMatrix3[2] == "0")):
        DrwaCheck = 1
        print(f"Congrats {name2} you won the match")
        printMatrix()
        break

    if ((gameMatrix1[0] == "0" and gameMatrix2[0] == "0" and gameMatrix3[0] == "0") or (
            gameMatrix1[1] == "0" and gameMatrix2[1] == "0" and gameMatrix3[2] == "0") or (
            gameMatrix1[2] == "0" and gameMatrix2[2] == "0" and gameMatrix3[2] == "0")):
        DrwaCheck = 1
        print(f"Congrats {name2} you won the match".center(50))
        printMatrix()
        break
    if ((gameMatrix1[0] == "0" and gameMatrix2[1] == "0" and gameMatrix3[2] == "0")):
        DrwaCheck = 1
        print(f"Congrats {name2} you won the match".center(50))
        printMatrix()
        break

    if ((gameMatrix1[2] == "0" and gameMatrix2[1] == "0" and gameMatrix3[0] == "0")):
        DrwaCheck = 1
        print(f"Congrats {name2} you won the match".center(50))
        printMatrix()
        break
    if ((gameMatrix1[1] == "0" and gameMatrix2[1] == "0" and gameMatrix3[1] == "0")):
        DrwaCheck = 1
        print(f"Congrats {name2} you won the match".center(50))
        printMatrix()
        break

    if j == 9:
        print("This match was draw !! Thanks for playing".center(50))
        break

