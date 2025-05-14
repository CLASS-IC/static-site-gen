import unittest

from helper_functions import *
from htmlnode import *
from textnode import *

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

    def test_multi_prop(self):
        node = LeafNode('p', 'value', {"id": "test", "href": "test"})
        self.assertEqual(node.to_html(), '<p id="test" href="test">value</p>')

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(new_nodes)
    def test_split_nodes_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        print(new_nodes)
    def test_split_multi_nodes_italic(self):
        nodes = []
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        nodes.append(node)
        n2 = TextNode("This is text with another  _not bold block_ word", TextType.TEXT)
        nodes.append(n2)
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        print(new_nodes)