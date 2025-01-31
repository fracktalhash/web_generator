from enum import Enum

class TextType(Enum):
    
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italics"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"