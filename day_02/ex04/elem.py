#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        res = super().__str__().replace('"', '&quot;')
        res = res.replace('<', '&lt;')
        res = res.replace('>', '&gt;')
        return res.replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag_type = tag_type
        self.attr = attr
        self.tag = tag
        self.content = []
        self.add_content(content if content is not None else Text(''))

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f'<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{self.__make_attr()}/>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            for el in str(elem).split('\n'):
                result += f'  {el}\n'

        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    class ValidationError(Exception):
        pass

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    title = Elem(tag='title', content=Text('"Hello ground!"'), tag_type='double')
    head = Elem(tag='head', content=title, tag_type='double')
    h1 = Elem(tag='h1', content=Text('"Oh no, not again!"'), tag_type='double')
    img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    body = Elem(tag='body', content=[h1, img], tag_type='double')
    html = Elem(tag='html', content=[head, body], tag_type='double')
    print(html)
