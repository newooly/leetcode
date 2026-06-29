"""
41. First Missing Positive https://leetcode.com/problems/first-missing-positive/description/
Hard
Given an unsorted integer array nums. Return the smallest positive integer
that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

import unittest


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Working:
        1.
        case 1: if [1, 2, 3] in n = 3 arr, ans = n+1 (straight starting at 1)
        case 2: if [7, 8, 9] in n = 3 arr, ans = 1 (straight not starting at 1)
        case 3: if [3, 4, 1] in n = 3 arr, high=4 > n=3, int in list (rand. with 1)
        case 4: if [1, -1, 2] in n= 3 arr, can treat as [1, 2] with same rules
        therefore, 1 < missing < n+1 (n being len arr with num>0 ints)

        2.
        2*O(n) is still O(n)

        3.
        can use existing arr to mark
        """

        # step 1, clean neg numbers T(n)
        nums = [num for num in nums if num > 0]

        # step 2, get n = len(nums) T(n) to avoid using in loop
        n = len(nums)

        # step 2, mark used T(n)
        for num in nums:
            # if not marked, mark
            marked_i = abs(num) - 1

            # if int in list & not marked
            if n > marked_i and nums[marked_i] > 0:
                nums[marked_i] *= -1

        # step 3, find first unmarked i
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return n + 1


class FirstMissingPositiveTest(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().firstMissingPositive([1, 2, 0]), 3)

    def test_example_two(self):
        self.assertEqual(Solution().firstMissingPositive([3, 4, -1, 1]), 2)

    def test_example_three(self):
        self.assertEqual(Solution().firstMissingPositive([7, 8, 9, 11, 12]), 1)

    def test_consecutive_positive_range_returns_next_integer(self):
        self.assertEqual(Solution().firstMissingPositive([1, 2, 3]), 4)

    def test_duplicate_values_still_return_smallest_missing_positive(self):
        self.assertEqual(Solution().firstMissingPositive([2, 2]), 1)


if __name__ == "__main__":
    unittest.main()
