from collections import defaultdict
from nose.tools import assert_equal

class PermutationsAlt(object):


    def is_permutation(self, str1, str2):

        if str1 is None or str2 is None:

            return False

        if len(str1) != len(str2):

            return False

        unique_counts1 = defaultdict(int)

        unique_counts2 = defaultdict(int)

        for char in str1:

            unique_counts1[char] += 1

        for char in str2:

            unique_counts2[char] += 1

        return unique_counts1 == unique_counts2





class TestPermutation(object):

    def test_permutation(self, func):

        assert_equal(func(None, 'foo'), False)

        assert_equal(func('', 'foo'), False)

        assert_equal(func('Nib', 'bin'), False)

        assert_equal(func('act', 'cat'), True)

        assert_equal(func('a ct', 'ca t'), True)

        print('Success: test_permutation')

def main():

    test = TestPermutation()

    permutations = Permutations()

    test.test_permutation(permutations.is_permutation)

    try:

        permutations_alt = PermutationsAlt()

        test.test_permutation(permutations_alt.is_permutation)

    except NameError:

        # Alternate solutions are only defined

        # in the solutions file

        pass


if __name__ == '__main__':

    main()