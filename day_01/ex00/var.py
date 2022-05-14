def print_type(el) -> None:
    print(f'{el} has a type {type(el)}')


def my_var():
    elements = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
    for el in elements:
        print_type(el)


if __name__ == '__main__':
    my_var()