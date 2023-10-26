import unittest

from bilibili import Bilibili


class TestBilibili(unittest.TestCase):
    def test_bilibili(self):
        bilibili = Bilibili("BV1Tw411F7A3")
        self.assertNotEqual(bilibili.video_urls._360P, None)
        self.assertNotEqual(bilibili.video_urls._480P, None)
