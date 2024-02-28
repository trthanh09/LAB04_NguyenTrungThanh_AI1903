import os
from datetime import datetime

def create_empty_file(file_name):
    with open(file_name, 'w') as file:
        pass
    print(f"Empty file '{file_name}' created.")

def create_file_with_datetime(file_name):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_with_datetime = f"{file_name}_{current_datetime}.txt"
    with open(file_with_datetime, 'w') as file:
        pass
    print(f"File with datetime '{file_with_datetime}' created.")

def create_file_with_permission(file_name, permission):
    with open(file_name, 'w') as file:
        pass
    os.chmod(file_name, permission)
    print(f"File '{file_name}' created with permission {permission}.")
create_empty_file("file")
create_file_with_datetime("datetime")
create_file_with_permission("any",112)