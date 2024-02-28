def write_to_new_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to new file '{file_name}'.")
def append_to_existing_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
    print(f"Content appended to existing file '{file_name}'.")
def write_list_to_file(file_name, lines):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print(f"List of lines written to file '{file_name}'.")
write_to_new_file("sales.txt", "content")