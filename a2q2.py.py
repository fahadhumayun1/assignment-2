###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name
# NSID
# Student Number

################### DO NOT ALTER CODE BELOW ###################################
def gcd(val1: int, val2: int) -> int:
    """
    Purpose: Find the greatest common divisor (gcd) of the two values passed in.
    Pre-conditions:
        :param val1: int - integer value being compared to find gcd.
            Must be less than 1000, else returns -1
        :param val2: int - integer value being compared to find gcd
            Must be less than 1000, else returns -1
    Post Conditions:
        None
    Return:
        int - The greatest common positive divisor of the two numbers passed in.
            -1 returned on failure.
    """
    return -1


def replace(input_str: str, target: str, replacement: str) -> str:
    """
    Purpose: Replace all instances of target string with replacement string within input string.
        Starting at the first occurrence of target string.
    Pre-condition
        :param input_str:str - input string to change target strings to replacement strings
        :param target: str - string that one wishes to change, if empty will return original string uncahnged.
        :param replacement: str - string that will replace target strings in the input string
    Post Condition:
        None
    Return:
        str - new string where target strings have been changed to replacement string
    """
    new_str = ""
    inp_len = len(input_str)
    targ_len = len(target)
    if inp_len < targ_len or targ_len==0:
        new_str = input_str
    else:
        i = 0
        while i < inp_len:
            if input_str[i:i+targ_len] == target:
                new_str += replacement
                i += targ_len
            else:
                new_str += input_str[i]
                i += 1
    return new_str


def grade_letter(score:int) -> str:
    """
    Purpose: Get the grade letter related to the score passed in.

    Pre-condition
        :param score:int - the number being calculated to a letter grade.
            Should be within the range of 0-100
    Post Condition:
        None
    Return:
        str - string associated with the score passed in
            if score is outside valid range returns the string "Invalid"
    """
    letter = ""
    if score < 0 or score > 100:
        letter = "Invalid"
    elif score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def sort_students_into_grades(student_list: list) -> dict:
    """
    Purpose: Goes through a list of dictionaries adding student names to the appropriate dictionary grade letter
        If the student's grade is not one of "A", "B", "C", "D", or "F", it is added to list "Invalid".
    Pre-condition:
        :param student_list: list of dictionaries,
            each dictionary represents a student and contains two keys: 'name' and 'grade'
    Post Condition:
        None
    Return:
        dict with lists as values; each key has a list value of names of students with that grade letter.
            Contains the keys "A","B","C","D","F","Invalid"
    """
    return {}
################### DO NOT ALTER CODE ABOVE ###################################


# TODO: Create tests for functions above
#test function for gcd
def test_gcd():
    # Test case 1: Valid inputs
    assert gcd(12, 18) == 6, "Test case 1 failed"

    # Test case 2: Valid inputs, one value is 0
    assert gcd(0, 25) == 25, "Test case 2 failed"

    # Test case 3: Invalid input, val1 > 1000
    assert gcd(1500, 50) == -1, "Test case 3 failed"

    # Test case 4: Invalid input, val2 > 1000
    assert gcd(50, 1500) == -1, "Test case 4 failed"

    # Test case 5: Invalid input, val1 and val2 > 1000
    assert gcd(1500, 1500) == -1, "Test case 5 failed"

    # Test case 6: Valid inputs, both values are prime numbers
    assert gcd(17, 23) == 1, "Test case 6 failed"

    print("All test cases passed for gcd()")

#after completing this commit

# test function for test_replace function
def test_replace():
    # Test case 1: Valid inputs, target string exists in input string
    assert replace("Hello, World!", "o", "x") == "Hellx, Wxrld!", "Test case 1 failed"

    # Test case 2: Valid inputs, target string does not exist in input string
    assert replace("Hello, World!", "z", "x") == "Hello, World!", "Test case 2 failed"

    # Test case 3: Empty target string, input string remains unchanged
    assert replace("Hello, World!", "", "x") == "Hello, World!", "Test case 3 failed"

    # Test case 4: Valid inputs, multiple occurrences of target string
    assert replace("Hello, Hello, Hello!", "Hello", "Hi") == "Hi, Hi, Hi!", "Test case 4 failed"

    print("All test cases passed for replace()")

    ###after completing this commit

    #test function for test_grade_letter


def test_grade_letter():
    # Test case 1: Valid input, score within range
    assert grade_letter(85) == "B", "Test case 1 failed"

    # Test case 2: Valid input, score at the lower boundary
    assert grade_letter(0) == "F", "Test case 2 failed"

    # Test case 3: Valid input, score at the upper boundary
    assert grade_letter(100) == "A", "Test case 3 failed"

    # Test case 4: Invalid input, score below range
    assert grade_letter(-10) == "Invalid", "Test case 4 failed"

    # Test case 5: Invalid input, score above range
    assert grade_letter(110) == "Invalid", "Test case 5 failed"

    print("All test cases passed for grade_letter()")

# test function for sor test_sort_students_into_grades
def test_sort_students_into_grades():
    # Test case 1: Valid input, multiple students with different grades
    student_list = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "C"},
        {"name": "Dave", "grade": "D"},
        {"name": "Eve", "grade": "F"},
        {"name": "Frank", "grade": "A"},
    ]
    expected_result = {
        "A": ["Alice", "Frank"],
        "B": ["Bob"],
        "C": ["Charlie"],
        "D": ["Dave"],
        "F": ["Eve"],
        "Invalid": []
    }
    assert sort_students_into_grades(student_list) == expected_result, "Test case 1 failed"

    # Test case 2: Valid input, empty student list
    assert sort_students_into_grades([]) == {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": [],
        "Invalid": []
    }, "Test case 2 failed"

    # after writing this function commit


    print("All test cases passed for sort_students_into_grades()")
# TODO Create test driver for whitebox tested functions
def test_driver_whitebox():
    # Test gcd()
    print("Testing gcd()...")
    print("gcd(12, 18) =", gcd(12, 18))  # Expected output: 6
    print("gcd(0, 25) =", gcd(0, 25))  # Expected output: 25
    print("gcd(1500, 50) =", gcd(1500, 50))  # Expected output: -1
    print("gcd(50, 1500) =", gcd(50, 1500))  # Expected output: -1
    print("gcd(1500, 1500) =", gcd(1500, 1500))  # Expected output: -1
    print("gcd(17, 23) =", gcd(17, 23))  # Expected output: 1
    print("gcd(0, 0) =", gcd(0, 0))  # Expected output: 0
    print()

    # Test replace()
    print("Testing replace()...")
    print('replace("Hello, World!", "o", "x") =', replace("Hello, World!", "o", "x"))  # Expected output: "Hellx, Wxrld!"
    print('replace("Hello, World!", "z", "x") =', replace("Hello, World!", "z", "x"))  # Expected output: "Hello, World!"
    print('replace("Hello, World!", "", "x") =', replace("Hello, World!", "", "x"))  # Expected output: "Hello, World!"
    print('replace("Hello, Hello, Hello!", "Hello", "Hi") =', replace("Hello, Hello, Hello!", "Hello", "Hi"))  # Expected output: "Hi, Hi, Hi!"
    print()

    # Test grade_letter()
    print("Testing grade_letter()...")
    print("grade_letter(85) =", grade_letter(85))  # Expected output: "B"
    print("grade_letter(0) =", grade_letter(0))  # Expected output: "F"
    print("grade_letter(100) =", grade_letter(100))  # Expected output: "A"
    print("grade_letter(-10) =", grade_letter(-10))  # Expected output: "Invalid"
    print("grade_letter(110) =", grade_letter(110))  # Expected output: "Invalid"
    print()

# Call the test driver
print("--------------Whitebox Test cases----------------------\n")
test_driver_whitebox()

# TODO: Create test driver for blackbox tested functions
def test_driver_blackbox():
    # Test gcd()
    print("Testing gcd()...")
    print("gcd(12, 18) =", gcd(12, 18))  # Expected output: 6
    print("gcd(0, 25) =", gcd(0, 25))  # Expected output: 25
    print("gcd(17, 23) =", gcd(17, 23))  # Expected output: 1
    print()

    # Test replace()
    print("Testing replace()...")
    print('replace("Hello, World!", "o", "x") =', replace("Hello, World!", "o", "x"))  # Expected output: "Hellx, Wxrld!"
    print('replace("Hello, Hello, Hello!", "Hello", "Hi") =', replace("Hello, Hello, Hello!", "Hello", "Hi"))  # Expected output: "Hi, Hi, Hi!"
    print()

    # Test grade_letter()
    print("Testing grade_letter()...")
    print("grade_letter(85) =", grade_letter(85))  # Expected output: "B"
    print("grade_letter(0) =", grade_letter(0))  # Expected output: "F"
    print("grade_letter(100) =", grade_letter(100))  # Expected output: "A"
    print()

    # Test sort_students_into_grades()
    print("Testing sort_students_into_grades()...")
    student_list = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "C"},
        {"name": "Dave", "grade": "D"},
        {"name": "Eve", "grade": "F"},
        {"name": "Frank", "grade": "A"},
    ]
    print("sort_students_into_grades(student_list) =", sort_students_into_grades(student_list))
    # Expected output: {
    #     "A": ["Alice", "Frank"],
    #     "B": ["Bob"],
    #     "C": ["Charlie"],
    #     "D": ["Dave"],
    #     "F": ["Eve"],
    #     "Invalid": []
    # }

    print()

# Call the test driver
print("--------------Blackbox Test cases----------------------\n")
test_driver_blackbox()
# TODO: Create test driver to test all functions
def test_driverBlackWhite():
    # Test gcd()
    print("Testing gcd()...")
    print("gcd(12, 18) =", gcd(12, 18))  # Expected output: 6
    print("gcd(0, 25) =", gcd(0, 25))  # Expected output: 25
    print("gcd(1500, 50) =", gcd(1500, 50))  # Expected output: -1
    print("gcd(50, 1500) =", gcd(50, 1500))  # Expected output: -1
    print("gcd(1500, 1500) =", gcd(1500, 1500))  # Expected output: -1
    print("gcd(17, 23) =", gcd(17, 23))  # Expected output: 1
    print("gcd(0, 0) =", gcd(0, 0))  # Expected output: 0
    print()
# Test replace()
    print("Testing replace()...")
    print('replace("Hello, World!", "o", "x") =', replace("Hello, World!", "o", "x"))  # Expected output: "Hellx, Wxrld!"
    print('replace("Hello, World!", "z", "x") =', replace("Hello, World!", "z", "x"))  # Expected output: "Hello, World!"
    print('replace("Hello, World!", "", "x") =', replace("Hello, World!", "", "x"))  # Expected output: "Hello, World!"
    print('replace("Hello, Hello, Hello!", "Hello", "Hi") =', replace("Hello, Hello, Hello!", "Hello", "Hi"))  # Expected output: "Hi, Hi, Hi!"
    print()

    # Test grade_letter()
    print("Testing grade_letter()...")
    print("grade_letter(85) =", grade_letter(85))  # Expected output: "B"
    print("grade_letter(0) =", grade_letter(0))  # Expected output: "F"
    print("grade_letter(100) =", grade_letter(100))  # Expected output: "A"
    print("grade_letter(-10) =", grade_letter(-10))  # Expected output: "Invalid"
    print("grade_letter(110) =", grade_letter(110))  # Expected output: "Invalid"
    print()

    # Test sort_students_into_grades()
    print("Testing sort_students_into_grades()...")
    student_list = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "C"},
        {"name": "Dave", "grade": "D"},
        {"name": "Eve", "grade": "F"},
        {"name": "Frank", "grade": "A"},
    ]
    print("sort_students_into_grades(student_list) =", sort_students_into_grades(student_list))
    # Expected output: {
    #     "A": ["Alice", "Frank"],
    #     "B": ["Bob"],
    #     "C": ["Charlie"],
    #     "D": ["Dave"],
    #     "F": ["Eve"],
    #     "Invalid": []
    # }

    print()
# Call the test driver
print("---------------------whitebox , blackbox all the test cases are printed below----------------------------------")
test_driverBlackWhite()


