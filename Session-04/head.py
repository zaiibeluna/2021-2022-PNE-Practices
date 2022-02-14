from pathlib import Path

filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    head = lines[0]
    print(f"First line of the '{filename}' file:\n{head}")
    
except FileNotFoundError:
    print(f"[Error]: file '{filename}' not found.")
except IndexError:
    print(f"[Error]: file '{filename}' is empty.")
