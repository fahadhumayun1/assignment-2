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
#    Debugging exercise, relevant to Chapter 3 and 7
###############################################################################

# TODO: Fill in your information below
# Student Name
# NSID
# Student Number

# Recall another name for a list of dictionaries is a record.

# TODO: PART A - Find and Fix Errors
def copy_list_of_lists(data: list) -> list:
    """
    Purpose: Deep copy a list passed in
    Pre-conditon:
        :param data : list - list to be copied,
            list can be nested, with a max list depth of 2 [[],[],..].
    Post Condition:
        None, original data should be unaltered.
    Return:
        list - a new list with new internal lists created by copying the
     information from the list passed in.
    """
    new_list = data
    return new_list

def copy_dict_of_dicts(data: dict) -> dict:
    """
    Purpose: Deep copy the dictionary passed in.
    Pre-conditon:
        :param data: dict() - dictionary to be copied,
            data can have values that are dictionaries,
            with a maximum depth of 2 {"OuterKey":{"innerKey":"InnerValue"}}.
    Post Condition:
        None, original data should be unaltered.
    Return:
        dict - a new dictionary with new internal dictionaries created by copying the
     information from the list passed in.
    """
    new_dict = {}
    for element in data:
        if data[element] is data:
            new_dict[element] = data[element]
    return new_dict


# TODO PART B - Implement the following functions based on the description

def deep_copy_list_of_dicts(data:list) -> list:
    """
    Purpose: Deep copy the list passed in.
    Pre-condition:
        :param data: list, list to be copied, if the list is not empty it contains dictionaries.
    Post Condition:
        None
    Return:
        list - deep copy of the list it's values are returned.
    """
    return []

def remove_from_2DList(data:list, val) -> list:
    """
    Purpose: Remove all instances of val from data
    Pre-condition:
        :param data: list - a two-dimensional list
        :param val: - The value to be removed if it exists.
    Post Condition:
        The list no longer contains
    Return:
        list - list with changes applied.
    """
    return []


def filter_from_2DList(data:list, val) -> list:
    """
    Purpose: Create a new list copied from data with all instances of val removed.
    Pre-condition:
        :param data: list - a two-dimensional list
        :param val: - The value to be filtered from new list.
    Post Condition:
        None
    Return:
        list - a new list with no instances of the value passed in.
    """
    return []

### TESTING ###


def test_partA():
    def test_ls():
        tests_ran = 0
        fails = 0
        # Empty List
        case1 = []
        case2 = [[], [3]]
        case3 = [[1, 2, 3, 5], ["a", "b", "c", "f"]]
        test_case = [
            {"input": case1,
            "output": copy_list_of_lists(case1),
            "reason": "Empty list should not impact functions success"},
            {"input": case2,
            "output": copy_list_of_lists(case2),
            "reason": "List with one internal list empty should still be able to be copied"},
            {"input": case3,
             "output": copy_list_of_lists(case3),
             "reason": "References should be different since it is a list of lists"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test List Copy\nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test List Copy\nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"].append([-1,2,4])
            if test["input"] == test["output"]:
                fails += 1
                print("Test List Copy\nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].remove([-1, 2, 4])

            # Just ran 3 tests
            tests_ran += 3

            # Checking internal lists are also deep copied
            if len(test["input"]) > 0 and len(test["input"][0]) > 0:
                tests_ran += 1
                popped = test["input"][-1].pop()
                if test["input"] == test["output"]:
                    fails += 1
                    print("Test List Copy\nERROR: Inner list values should no longer be the the same\n", test)
                # reset test["input"]
                test["input"][-1].append(popped)
        return tests_ran, fails

    def test_dict():
        tests_ran = 0
        fails = 0
        # Empty List
        case1 = {}
        case2 = {"a":{},
                 "b":{1:-1,
                      2:-2}}
        case3 = {"a": {1:0,
                       2:1,
                       3:2},
                 "b": {1: -1,
                       2: -2}}
        test_case = [
            {"input": case1,
            "output": copy_dict_of_dicts(case1),
            "reason": "Empty dict should not impact function success"},
            {"input": case2,
            "output": copy_dict_of_dicts(case2),
            "reason": "Dict with one internal blank dict should still be able to be copied"},
            {"input": case3,
             "output": copy_dict_of_dicts(case3),
             "reason": "References should be different for internal dicts too"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"]["c"]={"z":9}
            if test["input"] == test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].pop("c")

            # Just ran 3 tests
            tests_ran += 3

        # Checking internal lists are also deep copied
        tests_ran += 1
        case3["a"][1] = 9
        if case3 == test_case[2]["output"]:
            fails += 1
            print("Test Dict Copy\nERROR: Inner dict values should no longer be the the same\n", test)
        # reset case3
        case3["a"][1] = 0
        return tests_ran, fails
    ls_ran,ls_fail = test_ls()
    dict_ran, dict_fail = test_dict()
    return ls_ran + dict_ran, ls_fail, dict_fail


def test_partB():
    def test_lsdict():
        tests_ran = 0
        fails = 0
        case1 = []
        case2 = [{"a": 30,
                     "b": 50},
                 {}]
        case3 = [{"a":90,
                  "b":19},
                 {"a": 20,
                  "b": 12}]
        test_case = [
            {"input": case1,
             "output": deep_copy_list_of_dicts(case1),
             "reason": "Empty list should not impact function success"},
            {"input": case2,
             "output": deep_copy_list_of_dicts(case2),
             "reason": "Dict with one internal blank dict should still be able to be copied"},
            {"input": case3,
             "output": deep_copy_list_of_dicts(case3),
             "reason": "References should be different for internal dicts too"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"].append({"z":9})
            if test["input"] == test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].pop()
            # Just ran 3 tests
            tests_ran += 3
            # Checking internal dicts are also deep copied
            if len(test["input"]) > 0 and len(test["input"][-1]) > 0:
                tests_ran += 1
                test["input"][-1]["z"] = 8
                if test["input"] == test["output"]:
                    fails += 1
                    print("Test Deep Copy \nERROR: Inner list values should no longer be the the same\n", test)
                # reset test["input"]
                test["input"][-1].pop("z")
        return tests_ran, fails

    def test_remove():
        tests_ran = 0
        fails = 0
        case1 = [[],[4]]
        case2 = [[1,2,3],[45,2,14],[78,47,3,56],[9,3,7]]
        case3 = [[1,2,1],[1,2,3],[1,23,4],[1,21]]
        test_case = [
            {"input": (case1,4),
             "output": remove_from_2DList(case1,4),
             "reason": "Empty list should not impact function success"},
            {"input": (case1,2),
             "output": remove_from_2DList(case1,2),
             "reason": "Removing value that does not exist should not impact function success"},
            {"input": (case2,3),
             "output": remove_from_2DList(case2,3),
             "reason": "Lists of different sizes should not impact function success"},
            {"input": (case3,1),
             "output": remove_from_2DList(case3,1),
             "reason": "Internal lists should not impact function success"}
        ]
        for test in test_case:
            # Testing references should be same
            if test["input"][0] is not test["output"]:
                fails += 1
                print("Test Remove \nERROR: References are not the same\n", test)

            # Lists should still be equal
            if test["input"][0] != test["output"]:
                fails += 1
                print("Test Remove \nERROR: Values are not the same\n", test)

            # Changing list test["input"] should impact list in test["output"]
            test["input"][0].append([3])
            if test["input"][0] != test["output"]:
                fails += 1
                print("Test Remove \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"][0].pop()

            # Value should be removed from inner lists
            for inner in test["output"]:
                if test["input"][1] in inner:
                    fails += 1
                    print("Test Remove \nERROR: \n", test, "In internal list(s):\n",inner)

            # Just ran 4 tests
            tests_ran += 4
            # Checking internal lists are also shallow copied
            if len(test["input"][0]) > 0 and len(test["input"][0][0]) > 0:
                tests_ran += 1
                test["input"][0][0].append(8)
                if test["input"][0] != test["output"]:
                    fails += 1
                    print("Test Remove \nERROR: Inner list values should be the the same\n", test)
                # reset test["input"][0]
                test["input"][0][0].pop()
        return tests_ran, fails

    def test_filter():
        tests_ran = 0
        fails = 0
        case1 = [[], [4]]
        case2 = [[1, 2, 3], [45, 2, 14], [78, 47, 3, 56], [9, 3, 7]]
        case3 = [[1, 2, 1], [1, 2, 3], [3, 23, 4], [1, 1]]
        test_case = [
            {"input": (case1, 4),
             "output": filter_from_2DList(case1, 4),
             "reason": "Empty list should not impact function success"},
            {"input": (case1, 2),
             "output": filter_from_2DList(case1, 2),
             "reason": "Removing value that does not exist should not impact function success"},
            {"input": (case2, 3),
             "output": filter_from_2DList(case2, 3),
             "reason": "Lists of different sizes should not impact function success"},
            {"input": (case3, 1),
             "output": filter_from_2DList(case3, 1),
             "reason": "Internal lists should not impact function success"}
        ]
        for test in test_case:
            # Testing references should not be same
            if test["input"][0] is test["output"]:
                fails += 1
                print("Test Filter \nERROR: References are the same\n", test)

            # Changing list test["input"] should not impact list in test["output"]
            test["input"][0].append([3])
            if test["input"][0] == test["output"]:
                fails += 1
                print("Test Filter \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"][0].pop()

            # Value should be removed from inner lists
            for inner in test["output"]:
                if test["input"][1] in inner:
                    fails += 1
                    print("Test Filter \nERROR: \n", test, "In internal list(s):\n", inner)

            # Just ran 4 tests
            tests_ran += 4

            # Checking internal lists are also different references
            if len(test["input"][0]) > 0 and len(test["input"][0][-1]) > 0:
                tests_ran += 1
                test["input"][0][-1].append(8)
                if test["input"][0] == test["output"]:
                    fails += 1
                    print("Test Filter \nERROR: Inner list values should not be the the same\n", test)
                # reset test["input"][-1]
                test["input"][0][-1].pop()
        return tests_ran, fails

    lsdict_ran, lsdict_fail = test_lsdict()
    rm_ran, rm_fail = test_remove()
    filt_ran, filt_fail = test_filter()
    return lsdict_ran + rm_ran + filt_ran, lsdict_fail, rm_fail, filt_fail

def run_tests(run_all=False):
    def stats(Arun,Als,Adict,Brun,Bcp,Brm,Bflt):
        print("Total Tests Ran: ", Arun + Brun)
        print("PartA Tests Ran: ", Arun)
        print("PartA Fails:", Als + Adict)
        print("\t List of List Fails:", Als)
        print("\t Dict of Dicts Fails:", Adict)
        print("PartB Tests Ran: ", Brun)
        print("PartB Fails:", Bcp + Brm + Bflt)
        print("\t List of Dicts Fails:", Bcp)
        print("\t Remove From List Of List Fails:", Brm)
        print("\t Filter List Of List Fails:", Bflt)
        exit()
    PartARan, PartA_ls, PartA_dict = test_partA()
    if run_all:
        PartBRan, PartB_dpcp, PartB_rm, PartB_filt = test_partB()
        stats(PartARan, PartA_ls, PartA_dict, PartBRan, PartB_dpcp, PartB_rm, PartB_filt)
    if PartA_ls > 0:
        print("FINISH copy_list_of_lists BEFORE GOING ON")
        print("copy_list_of_lists HAS: ", PartA_ls, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartA_dict > 0:
        print("FINISH copy_dict_of_dicts BEFORE GOING ON")
        print("copy_dict_of_dicts HAS: ", PartA_dict, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    PartBRan, PartB_dpcp, PartB_rm, PartB_filt = test_partB()
    if PartB_dpcp > 0:
        print("FINISH deep_copy_list_of_dicts BEFORE GOING ON")
        print("deep_copy_list_of_dicts HAS: ", PartB_dpcp, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartB_rm > 0:
        print("FINISH remove_from_2DList BEFORE GOING ON")
        print("remove_from_2DList HAS: ", PartB_rm, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartB_rm > 0:
        print("FINISH filter_from_2DList BEFORE GOING ON")
        print("filter_from_2DList HAS: ", PartB_filt, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    else:
        stats(PartARan, PartA_ls, PartA_dict, PartBRan, PartB_dpcp, PartB_rm, PartB_filt)


if __name__ == '__main__':
    # TODO - Run to see what is working
    run_tests()
    # WARNING: Just because a test case passes does not mean there is not bugs present

