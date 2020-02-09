from unittest import TestCase
from jotIt.notes.tag import TagGroup
from jotIt.test.constants import *


class TestTag(TestCase):
    def setUp(self):
        self.tags = TagGroup(TAGS)

    def tearDown(self):
        self.tags = None

    def test_tag_contains(self):
        self.assertTrue(self.tags.contains(TAGS[0]))
        self.assertFalse(self.tags.contains("D"))

    def test_tag_sorts(self):
        self.assertEqual(self.tags.sorted(), sorted(TAGS))

    def test_add_tags(self):
        extra = ["D", "E"]
        self.tags.add_tags(extra)
        self.assertEqual(self.tags.getTags(), TAGS + extra)


if __name__ == "__main__":
    unittest.main()
