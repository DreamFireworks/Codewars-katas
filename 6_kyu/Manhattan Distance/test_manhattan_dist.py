def tester8321470(p1, p2):
    Test.it('Testing %s, %s' % (p1, p2))
    Test.assert_equals(manhattan_distance(p1, p2), abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

Test.describe('Fixed tests')
for item in ([1, 1], [1, 1]), ([5, 4], [3, 2]), ([1, 1], [0, 3]):
    tester8321470(*item)

from random import randint

Test.describe('Random tests')
for i in range(10):
  p1, p2 = [randint(0, 99), randint(0, 99)], [randint(0, 99), randint(0, 99)]
  tester8321470(p1, p2)