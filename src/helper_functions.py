import re
from htmlnode import *
from textnode import *


def text_node_to_html_node(text_node):
    val = text_node.text
    type = text_node.text_type

    if text_node is None:
        raise Exception("TextNode cannot be None")
    if type is text_node.text_type.TEXT:
        return LeafNode(tag=None, value=val)
    elif type is text_node.text_type.BOLD:
        return LeafNode(tag='b', value=val)
    elif type is text_node.text_type.ITALIC:
        return LeafNode(tag='i', value=val)
    elif type is text_node.text_type.CODE:
        return LeafNode(tag='code', value=val)
    elif type is text_node.text_type.LINK:
        return LeafNode(tag='a', value=val, props={"href": TextNode.URL})
    elif type is text_node.text_type.IMAGE:
        return LeafNode(tag='img', value='', props={"src": TextNode.URL, "alt": val})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if old_nodes is None:
        raise Exception("You need to pass in a list of nodes")

    if text_type is TextType.TEXT:
        return old_nodes

    for old_node in old_nodes:
        # Split the text by the delimiter
        parts = old_node.text.split(delimiter, 2)  # Split only on first two occurrences

        if len(parts) < 3:
            raise Exception(f"Could not split {old_node} because there is improper syntax with the delimiter: {delimiter}")
        n1 = TextNode(text=parts[0], text_type=TextType.TEXT)
        n2 = TextNode(text=parts[1], text_type=text_type)
        n3 = TextNode(text=parts[2], text_type=TextType.TEXT)

        new_nodes.extend([n1, n2, n3])

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches