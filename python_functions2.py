# a function that returns the maximum of three numbers
def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_num(1, 2, 3))

# function that multiplies all the numbers in a list
def multi_list(lst):
    if len(lst) == 0:
        return 0

    prod = lst[0] 

    if len(lst) > 1: 
        for i in lst[1:]: 
            prod = prod * i
    return prod

print(multi_list([1, 2, 3, 4]))
print(multi_list([]))
print(multi_list([13]))

#this function will reverse a string
def rev_string(my_str):
    return my_str[::-1]

print(rev_string("hello"))
print(rev_string("bear"))

#this function checks if a number falls within a range
def num_within(x,a,b):
    return x in range(a,b+1)

print(num_within(5,2,11))
print(num_within(3,4,9))

#a function which will print pascal's triangle out to n rows
triangle = [[1],[1,1]]
def pascal(n):
    #base case
    if n < 1:
        print("invalid input")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number-1]
            length = len(row_prev)+1
            for i in range(length):
                #first number is 1
                if i == 0:
                    row.append(1)
                #add numbers from previous row
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i - 1]  + triangle[row_number-1][i])
                #last number is also 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        #print triangle
        for row in triangle:
            print(row)

pascal(2)
pascal(5)