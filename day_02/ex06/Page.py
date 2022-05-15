from elements import Elem, HTML, Head, Body, Title, Meta, Img, Table, Tr, Th, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text


class Page:
    def __init__(self, elem):
        self.elem = elem

    def is_valid(self):
        return self._check_valid(self.elem)

    def __str__(self):
        if isinstance(self.elem, HTML):
            return f'<!DOCTYPE html>\n{self.elem}'
        return str(self.elem)

    def write_to_file(self, file_name):
        with open(file_name, 'w') as f:
            if isinstance(self.elem, HTML):
                f.write(f'<!DOCTYPE html>\n{self.elem}')
            else:
                f.write(str(self))

    def _check_valid(self, inst):
        if not self._check_in_elements(inst):
            return False
        res = []
        res.append(self._check_elem(inst))
        if isinstance(inst, Text):
            pass
        elif isinstance(inst.content, list):
            for el in inst.content:
                res.append(self._check_valid(el))
        elif inst.content:
            res.append(self._check_valid(inst.content))
        return all(res)

    @staticmethod
    def _check_elem(elem):
        if isinstance(elem, HTML):
            return len(elem.content) == 2 and isinstance(elem.content[0], Head) and isinstance(elem.content[1], Body)
        elif isinstance(elem, Head):
            return len(elem.content) == 1 and isinstance(elem.content[0], Title)
        elif isinstance(elem, (Body, Div)):
            return all(isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for el in elem.content)
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            return len(elem.content) == 1 and isinstance(elem.content[0], Text)
        elif isinstance(elem, P):
            return all(isinstance(el, Text) for el in elem.content)
        elif isinstance(elem, Span):
            return all(isinstance(el, (Text, P)) for el in elem.content)
        elif isinstance(elem, (Ul, Ol)):
            return all(isinstance(el, Li) for el in elem.content)
        elif isinstance(elem, Tr):
            return all(isinstance(el, Th) for el in elem.content) or all(isinstance(el, Td) for el in elem.content)
        elif isinstance(elem, Table):
            return all(isinstance(el, Tr) for el in elem.content)
        return True

    @staticmethod
    def _check_in_elements(elem):
        return isinstance(elem, (HTML, Head, Body, Title, Meta, Img, Table, Tr, Th, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text))


def test():
    page1 = Page(HTML(
                content=[
                    Head(content=Title(content=Text('"Hello ground!"'))),
                    Body(content=[
                        H1(content=Text('"Oh no, not again!"')),
                        Table(content=[
                            Tr(content=[Th(content=Text('Name')), Th(content=Text('Age'))]),
                            Tr(content=[Td(content=Text('Nik')), Td(content=Text('20'))]),
                            Tr(content=[Td(content=Text('Jora')), Td(content=Text('30'))]),
                        ]),
                        Div(content=Ol(content=[Li(content=Text('first')), Li(content=Text('second'))]))
                    ])
                ]))
    page2 = Page(Div(
        content=Span(content=Text('Test')),
    ))
    wrong_page1 = Page(HTML(content=Body(content=Div(content=Text('Wrong')))))
    wrong_page2 = Page(Table(content=Table(content=Tr(content=[Th(), Td(content=Text('wrong'))]))))
    return page1


if __name__ == '__main__':
    page = test()
    print(page.is_valid())
    print(page)
    page.write_to_file('test.html')
