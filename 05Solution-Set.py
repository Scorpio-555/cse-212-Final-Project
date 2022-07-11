'''
Set Problem to Solve Code Solution

Prompt:

Now using the new square circled in the image provided in the tutorial, do the following.

    * Create sets for the row, column and block that the new focus square resides in as demonstrated in the example problem.

    * Prompt the user to enter a number 1 - 9

    * If the number is valid, inform the user that the number has been added and then print the row, column and block showing that they now contain the user input.

    * Finally, if the number is not valid, inform the user why there was a conflict i.e., if the row, column and/or block already contains the number.
'''

#Create sets for row column and block

row_set = {8, 7, 9}

column_set = {3, 9, 6}

block_set = {6}

#Creating the sets one_thru_nine and numbers_used are an easy way to determine numbers_available.
#The set numbers_available is an easy way to check if the user's input is valid

one_thru_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}

numbers_used = row_set.union(column_set)
numbers_used = numbers_used.union(block_set)

numbers_available = one_thru_nine.symmetric_difference(numbers_used)

print(f"\nValid Numbers: {numbers_available}\n")

#Ask for user input

user_input = int(input("Type a Number 1 through 9: "))

#If the number is valid, inform the user that the number has been added
#then print the row, column and block showing that they now contain the user input
if user_input in numbers_available:
    row_set.add(user_input)
    column_set.add(user_input)
    block_set.add(user_input)

    print(f"\nThe number {user_input} has been added to the sudoku square")
    print(f"Current Numbers in Row: {row_set}")
    print(f"Current Numbers in Column: {column_set}")
    print(f"Current Numbers in Block: {block_set}\n")
else:
    #If the number is not valid, inform the user why there was a conflict 
    #i.e. if the row, column and/or block already contains the number.
    message = f"\nThere was a conflict. The number {user_input} was found in the same: | "
    if user_input in row_set:
        message = message + "Row | "
    if user_input in column_set:
        message = message + "Column | "
    if user_input in block_set:
        message = message + "Block | "
    
    print(f"{message}\n")
