# New tests for 3.8+
import codewars_test as test
from solution import square_digits

@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(3212), 9414)
        test.assert_equals(square_digits(2112), 4114)


@test.describe("Random Tests: ")
def random_tests():
    
    from random import randint
    
    def square_digits_test(number):
        new_number = ""
        for digit in str(number):
            digit = int(digit) ** 2
            new_number += str(digit)
        return int(new_number)
           
    for item in range(1, 101):
        randomtest = int(str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)))
        @test.it(f"testing for square_digits({randomtest})")
        def test_case():
            test.assert_equals(square_digits(randomtest), square_digits_test(randomtest))
        