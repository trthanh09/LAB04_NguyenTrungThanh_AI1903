def read_poem():
    try:
        with open("poem.txt", "r") as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    except FileNotFoundError:
        print("File 'poem.txt' not found.")
def count_lines_not_starting_with_t():
    try:
        with open("story.txt", "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if not line.strip().lower().startswith('t'):
                    count += 1
            print(f"Number of lines not starting with 'T': {count}")
    except FileNotFoundError:
        print("File 'story.txt' not found.")
read_poem()
count_lines_not_starting_with_t()