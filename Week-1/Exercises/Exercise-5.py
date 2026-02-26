# Helper function: Ignore
def sprint(s):
    if __name__ == "__main__":
        print(s)

################################################################################
"""
Recommended readings: 
  Chapter on functions: https://automatetheboringstuff.com/3e/chapter4.html
"""
################################################################################

"""
Exercise 5.1

Task:
------
Go back to the code you wrote for exercise 2.7 and turn it into a function called print_triangle_o.
The function should take one argument called 'rows' and print a triangle out of 'o's with n rows.
"""

sprint("Exercise 5.1")

def print_triangle_o(rows):
    for i in range(rows):
        print("{:^{}}".format("o"*((i+1)+i), (rows+(rows+1))))
    pass

print_triangle_o(10)
sprint("---")

"""
Exercise 5.2

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_easy.
You can assume that all the elements of the list are numbers.
"""

sprint("Exercise 5.2")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

def prod_list_easy(list_name):

    mult = 1
    for item in list_name:
        mult *= item
    return mult
    pass

print(prod_list_easy(lst))

sprint("---")

"""
Exercise 5.3

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_rec.
You can assume that all the elements of the list are numbers but you are not allowed to use
loops.

Hint: Can you think of a recursive way to do it?
------
"""

sprint("Exercise 5.3")

def prod_list_rec(list_name):
    """Returns the product of the elements in a number list recursively."""
    if len(list_name) == 1:
        return list_name[0]

    #base condition
    if list_name[:-1] == []:
        return list_name[-1]
    
    return list_name[-1]*prod_list_rec(list_name[:-1])
    pass

print(prod_list_rec(lst))
sprint("---")

"""
Exercise 5.4

Task:
------
Take the function body you wrote in the previous exercise and modify it so that it stops
executing in case not all of the elements of the list are numbers.

Hint: The product of the empty set is 1.
------
"""

sprint("Exercise 5.4")

test_list = [1, 4, -6, 7, 2, 3, 9, 11, 6, "bologna"]

def prod_list_rec_full(list_name):

    for item in list_name:
        if isinstance(item, (int, float)) != True:
            print("There are non-numerical items in this list")
            return

    if len(list_name) == 0:
        return print("There are no items in this list")
    
    if len(list_name) == 1:
        return list_name[0]

    if list_name[:-1] == []:
        return list_name[-1]
    
    return list_name[-1]*prod_list_rec(list_name[:-1])
    pass

print(prod_list_rec_full(test_list))
sprint("---")

"""
Exercise 5.5

Task:
------
Once you have solved Exercises 5.1 to 5.4, uncomment the following lines of code
and run the script again. The lines of code test the functions you wrote against
expected outputs. If you solved the exercises correctly, the script will tell you.
------
"""

### Run test cases
if __name__ == "__main__":
    from testcases import (
        #run_tests_ex51,
        run_tests_ex52,
        run_tests_ex53,
        run_tests_ex54,
    )
    #run_tests_ex51()
    run_tests_ex52()
    run_tests_ex53()
    run_tests_ex54()