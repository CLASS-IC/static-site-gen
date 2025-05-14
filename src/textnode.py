from enum import Enum

class TextType(Enum):
    TEXT = 'normal text'
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    def __repr__(self):
        if self.url:
            return f'TextNode("{self.text}", {self.text_type}, "{self.url}")'
        else:
            return f'TextNode("{self.text}", {self.text_type})'