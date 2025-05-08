import unittest
from lab7 import rabin_karp_search, haystack, needle


class TestRabinKarp(unittest.TestCase):
    def test_find(self):
        haystack = "abcdabcabc"
        needle = "abcd"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result , [0])


    def test_needle_len_higher_haystack_len(self):
        haystack = "ab"
        needle = "abc"
        result = rabin_karp_search(haystack , needle)
        self.assertEqual(result , [])

    def test_substring_not_found(self):
        haystack = "abcdef"
        needle = "gh"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])