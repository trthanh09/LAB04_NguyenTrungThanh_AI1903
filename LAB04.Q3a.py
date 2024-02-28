def file_operations(file_name):
    with open(file_name, 'r') as file:
        file.seek(0)
        content_at_beginning = file.read(30)  
        print(f"Content at the beginning of the file '{file_name}':\n{content_at_beginning}")
    with open(file_name, 'r') as file:
        file.seek(0, 2)  
        content_at_end = file.read(30) 
        print(f"\nContent at the end of the file '{file_name}':\n{content_at_end}")
    with open(file_name, 'r') as file:
        file.seek(10)  
        content_from_current = file.read(30)  
        print(f"\nContent after seeking first characters from the current position:\n{content_from_current}")
    with open(file_name, 'r') as file:
        file.seek(-20, 2)
        content_backward = file.read(30) 
        print(f"\nContent after seeking second characters backward from the end:\n{content_backward}")
    with open(file_name, 'r') as file:
        current_position = file.tell()
        print(f"\nCurrent position of the file handle in '{file_name}': {current_position}")
file_name = 'onlyfile.txt'
with open(file_name, 'w') as file:
    file.write("File chay thu khong biet co duoc hay khong nhung cu chay da")
file_operations(file_name)