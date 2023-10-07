from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def form(self):
        ...

class SimpleText(Text):
    def form(self):
        return "SimpleText"

class TextDecorator(Text):
    def __init__(self, text_object):
        self._text = text_object

    @abstractmethod
    def form(self):
        ...

class BoldDecorator(TextDecorator):
    def form(self):
        return self._text.form() + "+ Bold"

class ItalicDecorator(TextDecorator):
    def form(self):
        return self._text.form() + "+ Italic"

class UnderlineDecorator(TextDecorator):
    def form(self):
        return self._text.form() + "+ Underline"

def main():
    print("main!")

    #test

    simple_text = SimpleText()
    print(f"simple text: {simple_text.form()}")

    bold_text = BoldDecorator(simple_text)
    print(f"bold text: {bold_text.form()}")

    italic_text = ItalicDecorator(simple_text)
    print(f"italic text: {italic_text.form()}")

    underline_text = UnderlineDecorator(simple_text)
    print(f"underline text: {underline_text.form()}")

if __name__ == "__main__":
    main()
