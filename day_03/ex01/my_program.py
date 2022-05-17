from path import Path

def main():
    try:
        Path.makedirs('local_dirs')
    except FileExistsError as e:
        print(e)
    Path.touch('local_dirs/local_file.txt')
    f = Path('local_dirs/local_file.txt')
    f.write_lines(['local!'])
    print(f.read_text())

if __name__ == '__main__':
    main()