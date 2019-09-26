from unittest import TestCase

from twig_education_coding_test.twig_coding_test import group_list_elements


class TestGroupListElements(TestCase):

    def test_group_list_elements_correct_input(self):
        # Checking case as described in the coding challenge pseudo-code.
        self.assertEqual(
            group_list_elements([1, 2, 3, 4, 5], 3),
            [[1, 2], [3, 4], [5]]
        )
        self.assertEqual(
            group_list_elements([5, 4, 3, 2, 1], 2),
            [[5, 4], [3, 2, 1]]
        )
        # Check that this algorithm is type-agnostic.
        self.assertEqual(
            group_list_elements(['a', 2, 'c'], 1),
            [['a', 2, 'c']]
        )
        # Check that splitting into elements of length 1 also works for chars.
        self.assertEqual(
            group_list_elements(['a', 'b', 'c'], 3),
            [['a'], ['b'], ['c']]
        )
        # Check that a list containing sub-lists works as expected.
        self.assertEqual(
            group_list_elements([[1, 2, 3], [3, 2, 1], ['a', 'b', 'c'],
                                 ['c', 'd', 'e'], [4, 5, 6], [7, 8, 9]], 3),
            [[[1, 2, 3], [3, 2, 1]],
             [['a', 'b', 'c'], ['c', 'd', 'e']],
             [[4, 5, 6], [7, 8, 9]]]
        )
        # Check that a remainder of bigger than length 1 works.
        self.assertEqual(
            group_list_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 6),
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12, 13]]
        )
        # Check that splitting by a value larger than the length of the list
        # gives a list back which is split evenly - again unsure on the
        # desired behaviour, logic could be changed to instead return a 100
        # element list with empty lists for any elements after the ones
        # containing something.
        self.assertEqual(
            group_list_elements([1, 2, 3, 4, 5], 100),
            [[1], [2], [3], [4], [5]]
        )
        # Check that splitting by 0 returns an empty list - unsure if desired
        # behaviour, argument could be made to return the passed list instead.
        self.assertEqual(
            group_list_elements([1, 2, 3, 4, 5], 0),
            []
        )
        # Also check that splitting by 1 returns the list that we want to chunk
        # keeping in line with the pseudo-code example input / output.
        self.assertEqual(
            group_list_elements([1, 2, 3, 4, 5], 1),
            [[1, 2, 3, 4, 5]]
        )
        # Check that splitting an empty list just gives an empty list back.
        self.assertEqual(
            group_list_elements([], 5),
            []
        )
