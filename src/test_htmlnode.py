import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):

# Start of HTMLNode Tests
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

# Start of LeafNode tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Hello, world!</a>')

# Start of ParentNode Tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )