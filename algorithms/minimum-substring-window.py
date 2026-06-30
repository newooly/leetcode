"""
Minimum Window Substring https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t
(including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation:
    The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Sliding window with lookup table
        """

        if not s or not t:
            return ""

        # record required chars from t
        lookup = defaultdict(int)
        for letter_i in t:
            lookup[letter_i] += 1

        start_i = 0
        end_i = 0

        # record chars currently inside window
        window = defaultdict(int)

        # number of required chars from t that are satisfied in the window
        # includes duplicates, but does not count extra duplicates
        matched = 0

        min_substr = ""

        while end_i < len(s):
            # expand window by recording end letter
            current_s_letter = s[end_i]

            if current_s_letter in lookup:
                window[current_s_letter] += 1

                # only count this char if it was still needed
                # e.g. for t = "AB", the second "A" in "AAB" should not count
                if window[current_s_letter] <= lookup[current_s_letter]:
                    matched += 1

            # move end_i
            end_i += 1

            # if all chars in t seen in window,
            # shrink from the start while the window is still valid
            while matched == len(t):
                # record min_substr
                curr_substr = s[start_i:end_i]
                if not min_substr or len(curr_substr) < len(min_substr):
                    min_substr = curr_substr

                # move start_i
                curr_s_letter = s[start_i]

                if curr_s_letter in lookup:
                    window[curr_s_letter] -= 1

                    # if removing this char makes the window miss a required char,
                    # the window is no longer valid
                    if window[curr_s_letter] < lookup[curr_s_letter]:
                        matched -= 1

                start_i += 1

        return min_substr


if __name__ == "__main__":
    print(Solution().minWindow(s="AAB", t="AB"))
