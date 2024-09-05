import os

def write_file(file_name, file_content):
    """
    Creates of overwrites a .txt file with the provided file content.
    """
    full_file_name = f"{file_name}.txt"

    with open(full_file_name, mode="w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends provided content to a .txt file.
    """
    full_file_name = f"{file_name}.txt"

    with open(full_file_name, mode="a", encoding="utf-8") as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads and returns content of the .tx file.
    """
    full_file_name = f"{file_name}.txt"

    # Read the content from the file
    if os.path.exists(full_file_name):
        with open(full_file_name, mode="r", encoding="utf-8") as file:
            return file.read()
    else:
        return "File does not exist."
