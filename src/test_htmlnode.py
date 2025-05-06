import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_equality(self):
        node1 = HtmlNode('tag', 'value', [], {})
        node2 = HtmlNode('tag', 'value', [], {})
        self.assertEqual(node1, node2)
    def test_inequality(self):
        node1 = HtmlNode('tag', 'value', [], {})
        node2 = HtmlNode('tag', 'different value', [], {})
        self.assertNotEqual(node1, node2)
    def test_children(self):
        node1 = HtmlNode('tag', 'value', [], {})
        node2 = HtmlNode('tag', 'value', ['test', 'new'], {})
        self.assertNotEqual(node1, node2)
    def test_props(self):
        node1 = HtmlNode('tag', 'value', [], {})
        node2 = HtmlNode('tag', 'value', [], {"key": "value"})
        self.assertNotEqual(node1, node2)