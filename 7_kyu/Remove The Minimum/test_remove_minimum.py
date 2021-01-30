Test.describe("remove_smallest")

Test.it("works for the examples")
Test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
Test.assert_equals(remove_smallest([1, 2, 3, 4]), [2, 3, 4], "Wrong result for [1, 2, 3, 4]")
Test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
Test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
Test.assert_equals(remove_smallest([]), [], "Wrong result for []")

from numpy.random import randint
from random import choice  

def randlist():
    return list(randint(400, size=randint(1, 10)))

def solution(numbers):
    if not numbers: return numbers
    
    numbers = numbers[:]
    numbers.remove(min(numbers))
    return numbers


Test.it("returns [] if list has only one element")
for i in range(10):
    x = randint(1, 400)
    Test.assert_equals(remove_smallest([x]), [], "Wrong result for [{}]".format(x))
    
Test.it("returns a list that misses only one element")
for i in range(10):
    arr = randlist()
    if randint(0, 1): arr[randint(0, len(arr) - 1)] = min(arr)
    Test.assert_equals(len(remove_smallest(arr[:])), len(arr) - 1, "Wrong sized result for {}".format(arr))
    
Test.it("check for mutations to original list")    
a = randlist() # generates the list
b = list(a) # makes a swallow copy
remove_smallest(a) # uses the original list with the function
Test.assert_equals(a, b, "You've mutated input list") # test the list match

Test.it("works for random lists")
for i in range(20):
    arr = randlist()
    Test.assert_equals(remove_smallest(arr[:]), solution(arr), "Wrong result for {}".format(arr))