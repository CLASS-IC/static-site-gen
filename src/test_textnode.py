import unittest

#from htmlnode import *
#from helper_functions import *
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('test', TextType.BOLD)
        node2 = TextNode('test', TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text(self):
        node = TextNode('test', TextType.BOLD)
        node2 = TextNode('test not equal', TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_urls(self):
        node = TextNode('test', TextType.BOLD)
        node2 = TextNode('test', TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)
    def test_type(self):
        node = TextNode('test', TextType.BOLD)
        node2 = TextNode('test', TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()