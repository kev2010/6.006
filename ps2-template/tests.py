import unittest
from closest_pair import closest_pair

tests = (
    (
        [(-7, 9), (-8, -1), (-5, -5)],
        25
    ),
    (
        [(15, -15), (-16, -1), (8, 2), (16, 3), (-20, 13), (-6, 18)],
        65
    ),
    (
        [(-16, -30), (29, -27), (-28, -26), (-5, -19), (0, -16), (-2, -6), (28, -3), (-13, 1), (-4, 10), (-14, 17)],
        34
    ),
    (
        [(24, -45), (-25, -43), (-36, -41), (0, -37), (-9, -35), (33, -31), (-34, -30), (-23, -26), (23, -25), (15, -20), (28, -9), (-10, -3), (-28, 1), (-45, 16), (-35, 17), (44, 20), (22, 22), (-11, 42), (20, 43), (16, 45)],
        20
    ),
    (
        [(-4, -90), (-47, -89), (44, -88), (17, -85), (-28, -82), (60, -78), (88, -76), (89, -73), (-64, -63), (86, -59), (4, -58), (-44, -54), (-83, -53), (-54, -46), (-72, -45), (18, -44), (-74, -38), (58, -30), (84, -28), (-49, -26), (-38, -24), (87, -23), (50, -22), (33, -18), (14, -17), (74, -10), (-59, -9), (-29, -8), (-17, -1), (-3, 4), (-71, 12), (69, 14), (-32, 16), (68, 28), (2, 31), (-69, 36), (-57, 45), (11, 46), (-40, 54), (25, 55), (52, 67), (61, 68), (27, 69), (49, 72), (-79, 75), (-39, 76), (-60, 77), (82, 82), (-48, 87), (-53, 88)],
        10
    )
)

def check(points, min_d):
    return min_d == closest_pair(points)

class TestClosestPair(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0][0], tests[0][1]))

    def test_02(self):
        self.assertTrue(check(tests[1][0], tests[1][1]))

    def test_03(self):
        self.assertTrue(check(tests[2][0], tests[2][1]))

    def test_04(self):
        self.assertTrue(check(tests[3][0], tests[3][1]))
       
    def test_05(self):
        self.assertTrue(check(tests[4][0], tests[4][1]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
