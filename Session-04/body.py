from pathlib import Path

filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    print("Body of the '{filename}' file: ")
    for line in body:
      print(line)
except FileNotFoundError:
    print(f"[Error]: file '{filename}' not found.")
except IndexError:
    print(f"[Error]: file '{filename}' is empty.")