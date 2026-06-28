# Purpose: To test unittest framework
# Easy problem: Two Sum
# https://leetcode.com/problems/two-sum/

import unittest


class Solution:
    def twoSum(self, nums, target):
        """
        Find two numbers in `nums` that add up to `target`.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


class TwoSumTest(unittest.TestCase):
    def test_example(self):
        result = Solution().twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
