"""
permutation-sequence https://leetcode.com/problems/permutation-sequence/

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"
"""

import unittest


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str

        Time:  O(n²)
        Space: O(n)
        """
        # number of perms for n = n!
        # e.g. if n=3, numbers are [1,2,3], k = 5

        # build nums and calculate n!
        res_nums = []
        factorial = 1

        # start with n!
        # ex. loop will end with i=n=3, factorial = 3! = 6
        for i in range(1, n + 1):
            res_nums.append(i)
            factorial *= i

        # kth is 1-indexed, but list indexes are 0-indexed
        k -= 1

        res = ""

        # n=3, j range: 3,2,1
        for j in range(n, 0, -1):
            # reduce factorial, j=3, factorial=2!=2
            factorial //= j

            # index = 5//2 = 1, therefore [1,2,3][1] = 2 is the indexed val
            index = k // factorial

            # add indexed number to res
            res += str(res_nums.pop(index))

            # remove used factorial index
            # prev [1, 2, 3] uses 3! perms, new [1, 3] uses [2!] perms
            k %= factorial

        return res


class PermutationSequenceTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(Solution().getPermutation(3, 3), "213")

    def test_first_permutation(self):
        self.assertEqual(Solution().getPermutation(4, 1), "1234")

    def test_last_permutation(self):
        self.assertEqual(Solution().getPermutation(3, 6), "321")

    def test_non_trivial_mid_sequence(self):
        self.assertEqual(Solution().getPermutation(4, 9), "2314")


if __name__ == "__main__":
    unittest.main()
