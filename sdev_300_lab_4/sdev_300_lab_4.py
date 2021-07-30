"""
Allow user to enter and validate their phone number and zipcode+4
Enter values of two, 3x3 matrices
select from , addition, subtraction,matrix multiplication,
 and element by element multiplication
"""
import re
import sys
import numpy as np


def continue_matrix_game_check():
    """Function to ask the user if they would like to continue the program"""
    while True:
        play_game = input("Do you want to play the Matrix Game?\n"
                          "Enter 'Y' for Yes or 'N' for No:").lower()
        if play_game == "n":
            print("*************** Thanks for playing Python Numpy *******************")
            sys.exit()
        elif play_game == "y":
            break
        else: # ensure the user enters either 'y' or 'n'. If not, re-run.
            print("\nThat is not a valid entry. Please try again.")


def phone_number_entry():
    """Function to take down the users phone number"""
    phone_number = input("\nEnter your phone number (XXX-XXX-XXXX):")

    while True:
        # Ensure the user entry matches the correct format. If not, re-run.
        if not re.match("\\d{3}[-]\\d{3}[-]\\d{4}", phone_number):
            phone_number = input("That is not a valid phone number. Please try again."
                                 "(xxx-xxx-xxxx): ")
        else:
            print("\nYour phone number is:" + phone_number)
            break


def zip_code_entry():
    """Function to take down the users zip code"""
    zip_code = input("\nEnter your zip code+4 (XXXXX-XXXX):")

    while True:
        # Ensure the user entry matches the correct format. If not, re-run.
        if not re.match("\\d{5}[-]\\d{4}", zip_code):
            zip_code = input("That is not a valid zip code. Please try again."
                             "(XXXXX-XXXX):")
        else:
            print("\nYour zip code is: " + zip_code)
            break


def create_matrix():
    """Function to take the users entry for a matrix and return it"""
    matrix = np.zeros((3, 3)) # create multi-dimensional 3x3 array with zeros
    print("\nPlease create your matrix one entry at a time.\n"
          "Please start with your entries for row 1.")

    for row in range(3):
        for column in range(3):
            # continue until matrix is full
            flag = False

            while not flag:
                num = input(">>> ") # take user input for each row/column
                try:
                    # Ensure the user entry is an integer or float
                    float(num)
                    break
                except ValueError:
                    print("Please check your entry.  It must be a number.")
            # Add user entries to the matrix.
            matrix[row, column] = float(num)
        print("--------------------")  # seperate each row entry
    return matrix


def matrix_menu():
    """Function to print out the matrix menu"""
    print("\n1: Addition")
    print("2: Subtraction")
    print("3: Matrix Multiplication")
    print("4: Element by element multiplication")


def addition():
    """Function to add two matrix's"""
    addition_ans = matrix_1 + matrix_2
    return addition_ans


def subtraction():
    """Function to subtract two matrix's"""
    subtraction_ans = matrix_1 - matrix_2
    return subtraction_ans


def matrix_multiplication():
    """Function to multiply two matrix's"""
    matrix_multiply = np.matmul(matrix_1, matrix_2)
    return matrix_multiply


def element_multiplication():
    """Function to multiply individual elements of two matrix's"""
    element_multiply = np.multiply(matrix_1, matrix_2)
    return element_multiply


def transpose(transpose_matrix):
    """Function to transpose and print a matrix"""
    print("The Transpose is: ")
    print(transpose_matrix.transpose())


def matrix_mean(find_mean):
    """Function to find and print the mean of a matrix"""
    print("\nThe row and column mean values of the results are:")
    print("Rows: ")
    # Find mean of the rows
    print(np.mean(find_mean, 0))

    print("Columns: ")
    # Find mean of the columns
    print(np.mean(find_mean, 1))


print("*************** Welcome to the Python Matrix Application***********")

continue_matrix_game_check()

phone_number_entry()

zip_code_entry()

print("\nEnter your first 3x3 matrix:")
# Create the first matrix and output it
matrix_1 = create_matrix()
print("Your first matrix is:\n")
np.set_printoptions(precision=2) # ensure the matrix's are only 2 decimal places
print(matrix_1)

print("\nEnter your second 3x3 matrix:")
# Create the second matrix and output it
matrix_2 = create_matrix()
print("Your second matrix is:\n")
print(matrix_2)

while True:
    matrix_menu()
    choice = input(">>> ")

    if choice == "1":
        results = addition()
        print(results, "\n")

        # use transpose function with addition function to output the transposition
        transpose(addition())

        # Use matrix_mean function with addition function to output the mean
        matrix_mean(addition())
        continue_matrix_game_check()

    elif choice == "2":
        results = subtraction()
        print(results, "\n")

        # use transpose function with subtraction function to output the transposition
        transpose(subtraction())

        # Use matrix_mean function with subtraction function to output the mean
        matrix_mean(subtraction())
        continue_matrix_game_check()

    elif choice == "3":
        results = matrix_multiplication()
        print(results, "\n")

        # use transpose function with matrix_multiplication function to output the transposition
        transpose(matrix_multiplication())

        # Use matrix_mean function with matrix_multiplication function to output the mean
        matrix_mean(matrix_multiplication())
        continue_matrix_game_check()

    elif choice == "4":
        results = element_multiplication()
        print(results, "\n")

        # use transpose function with element_multiplication function to output the transposition
        transpose(element_multiplication())

        # Use matrix_mean function with element_multiplication function to output the mean
        matrix_mean(element_multiplication())
        continue_matrix_game_check()
