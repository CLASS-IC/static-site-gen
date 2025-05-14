from textnode import *

class HtmlNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        # This will loop through all props and return them properly formatted w/ a leading space
        return ''.join(f' {k}="{v}"' for k, v in self.props.items())

    def leading_tag(self):
        props_string = self.props_to_html()
        return f'<{self.tag}{props_string}>'

    def closing_tag(self):
        return f'</{self.tag}>'

    def __repr__(self):
        return f'HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})'

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(
            tag=tag,
            value=value,
            children=[],
            props=props if props is not None else {}
        )

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f'{self.value}'
        if self.props:
            props_string = self.props_to_html()
            return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(
            tag=tag,
            children=children,
            props=props if props is not None else {}
        )

    def to_html(self):
        if self.children is None:
            raise ValueError("All parents must have a children")
        if self.tag is None:
            raise ValueError("All parents must have a tag")
        #props_string = self.props_to_html()
        leading_tag = self.leading_tag()
        closing_tag = self.closing_tag()
        # Loops through all ChildNodes (LeafNodes), calls the .to_html() function for the child and then combines it all into 1 string
        inner_html = ''.join(child.to_html() for child in self.children)
        # Properly formats the ParentNode, but it doesnt do it beautifully
        return f'{leading_tag}{inner_html}{closing_tag}'

## Misc Functions

