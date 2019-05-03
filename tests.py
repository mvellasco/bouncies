from unittest import TestCase

from bouncy_numbers.core import is_bouncy, find_least_bouncy_number


class TestIsBouncy(TestCase):
    def test_538_is_bouncy(self):
        self.assertTrue(is_bouncy(538))

    def test_1587000_is_bouncy(self):
        self.assertTrue(is_bouncy(1587000))

    def test_155349_is_bouncy(self):
        self.assertTrue(is_bouncy(155349))


class TestIsNotBouncy(TestCase):
    def test_134468_is_not_bouncy(self):
        self.assertFalse(is_bouncy(134468))

    def test_1334_is_not_bouncy(self):
        self.assertFalse(is_bouncy(1334))

    def test_112_is_not_bouncy(self):
        self.assertFalse(is_bouncy(112))


class TestFindLeastBouncyNumber(TestCase):
    resp = find_least_bouncy_number()

    def test_least_number_is_1587000(self):
        self.assertEqual(self.resp[0], 1587000)

    def test_proportion_is_99_percent(self):
        self.assertEqual(self.resp[1], 99.0)
