from textnode import TextNode
from textnode import TextType


def main():
    new_text = TextNode("this is a new text", TextType.LINK, "https://www.google.com")
    print(new_text)

if __name__ == "__main__":
    main()