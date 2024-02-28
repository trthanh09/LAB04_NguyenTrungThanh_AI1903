def count_uppercase_characters(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print(f"Number of uppercase characters in the file: {uppercase_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
def count_specific_words(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read().lower()
            count_this = content.count("this")
            count_these = content.count("these")
            print(f"Number of occurrences of 'this': {count_this}")
            print(f"Number of occurrences of 'these': {count_these}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
count_uppercase_characters("article.txt")
count_specific_words("article.txt")