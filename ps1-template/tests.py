import unittest
from search_sorted_2D_array import search_sorted_2D_array

tests = (
    (
        ((0, 1, 3),
         (2, 4, 6),
         (5, 7, 8)),
        3
    ),
    (
        ((0, 1, 4, 7),
         (1, 3, 4, 8),
         (2, 6, 6, 8),
         (6, 8, 8, 9)),
        4
    ),
    (
        ((1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8)),
        5
    ),
    (
        ((1,  2,  5,  35, 44, 49, 50),
         (5,  10, 20, 46, 61, 61, 62),
         (8,  19, 38, 49, 65, 69, 77),
         (11, 33, 40, 65, 68, 70, 80),
         (17, 38, 42, 65, 68, 71, 89),
         (19, 42, 58, 76, 77, 80, 93),
         (30, 44, 59, 79, 86, 87, 95)),
        42
    ),
    (
        ((2,  6,  7,  8,  9,  15, 19, 19, 20),
         (8,  9,  19, 20, 43, 48, 50, 53, 56),
         (13, 22, 22, 25, 57, 60, 73, 75, 84),
         (23, 25, 35, 39, 58, 60, 73, 81, 89),
         (24, 26, 42, 60, 60, 65, 84, 91, 91),
         (26, 30, 42, 62, 76, 80, 87, 94, 94),
         (30, 41, 47, 69, 79, 81, 93, 95, 96),
         (52, 55, 55, 70, 81, 86, 93, 97, 97),
         (64, 67, 73, 74, 82, 88, 96, 99, 99)),
        87
    )
)

def check_search(A, v):
    # Note, this checker does not validate correctly when output is None
    location = search_sorted_2D_array(A, v)
    if location is not None:
        (x, y) = location
        return A[y][x] == v
    return False

class TestSearch2D(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check_search(tests[0][0], tests[0][1]))

    def test_02(self):
        self.assertTrue(check_search(tests[1][0], tests[1][1]))

    def test_03(self):
        self.assertTrue(check_search(tests[2][0], tests[2][1]))

    def test_04(self):
        self.assertTrue(check_search(tests[3][0], tests[3][1]))
       
    def test_05(self):
        self.assertTrue(check_search(tests[4][0], tests[4][1]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
