def generate_html(data) -> str:
    result = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>MyGenerate</title>
    </head>
    <body>
    <table><tr>
    '''
    current = 0
    for key, value in data.items():
        empty = 0
        if int(value[0]) < current:
            result += '</tr><tr>'
            current = int(value[0])
        if int(value[0]) > current:
            empty = int(value[0]) - current - 1
            current = int(value[0])
        for _ in range(empty):
            result += '<td style="border: 1px solid black; padding: 10px"></td>'
        result += f'''
        <td style="border: 1px solid black; padding: 10px">
        <h4>{key}</h4>
        <ul>
        <li>No {value[1]}</li>
        <li>{value[2]}</li>
        <li>{value[3]}</li>
        <li>{value[4]} electron</li>
        </ul>
        </td>'''
    result += '''</tr></table></body>'''
    return result


def periodic_table():
    data_dict = {}
    with open('day_01/ex07/periodic_table.txt', 'r') as f: #TODO change path
        elements = f.readlines()
        for el in elements:
            name, param = el.split('=', 1)
            data_dict[name] = [el.split(':', 1)[1] for el in map(str.strip, param.split(','))]
    with open('periodic_table.html', 'w') as f:
        f.write(generate_html(data_dict))


if __name__ == '__main__':
    periodic_table()