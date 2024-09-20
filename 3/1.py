file = "in.txt"
def print_file(mode):
    try:
        with open(file, 'r') as f:
            if mode == "line":
                print(f.read())
            elif mode == "full":
                for line in f:
                    print(line)
    except FileNotFoundError:
        print("файл не найден")

print_file('full')