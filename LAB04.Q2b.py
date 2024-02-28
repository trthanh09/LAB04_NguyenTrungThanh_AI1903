def count_total_words(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            total_words = len(words)
            print(f"Total number of words in the file: {total_words}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
def display_words_less_than_4_characters(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            short_words = [word.strip() for line in lines for word in line.split() if len(word) < 4]
            print("Words less than 4 characters:")
            print(', '.join(short_words))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
count_total_words("story.txt")
display_words_less_than_4_characters("story.txt")