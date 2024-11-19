import unittest
import group


class TestCases(unittest.TestCase):

    def test_groups_of_3_1(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = group.groups_of_3(input)
        self.assertEqual(expected, result)

    def test_groups_of_3_2(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        result = group.groups_of_3(input)
        self.assertEqual(expected, result)





if __name__ == "__main__":
    unittest.main()
