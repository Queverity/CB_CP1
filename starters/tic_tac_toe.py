# CB 1st Tic Tac Toe Starter
import random



playing = True

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

def win_condition(board):
     if board[0] == "X":
         return 1

print("Welcome to tic tac toe!")

while playing:
    print(row1)
    print(row2)
    print(row3)
    user_input = int(input("Where would you like to go?"))
    if user_input in row1:
        if user_input == 1:
            if row1[0] == "X" or row1[0] == "O":
                print("Spot is already taken.")
                continue
            row1[0] = "X"
        elif user_input == 2:
            if row1[1] == "X" or row1[1] == "O":
                print("Spot is already taken.")
                continue
            row1[1] = "X"
        elif user_input == 3:
            if row1[2] == "X" or row1[2] == "O":
                print("Spot is already taken.")
                continue
            row1[2] = "X"
    elif user_input in row2:
        if user_input == 4:
            if row2[0] == "X" or row2[0] == "O":
                print("Spot is already taken.")
                continue
            row2[0] = "X"
        elif user_input == 5:
            if row2[1] == "X" or row2[1] == "O":
                print("Spot is already taken.")
                continue
            row2[1] = "X"
        elif user_input == 6:
            if row2[2] == "X" or row2[2] == "O":
                print("Spot is already taken.")
                continue
            row2[2] = "X"
    elif user_input in row3:
        if user_input == 7:
            if row3[0] == "X" or row3[2] == "O":
                print("Spot is already taken.")
                continue
            row3[0] = "X"
        elif user_input == 8:
            if row3[1] == "X" or row3[2] == "O":
                print("Spot is already taken.")
                continue
            else:
                row3[1] = "X"
        elif user_input == 9:
            if row3[2] == "X" or row3[2] == "O":
                print("Spot is already taken.")
                continue
            else:
                row3[2] = "X"
    elif user_input not in row1 and user_input not in row2 and user_input not in row3:
        print("Invalid answer")
        continue
