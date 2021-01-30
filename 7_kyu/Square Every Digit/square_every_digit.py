"""
Task:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    x=[int(n) for n in str(num)]
    l=len(x)
    y=[]
    for j in range(l):
       y.append(x[j]**2) 
    y1 = [str(i) for i in y]
    return int("".join(y1))