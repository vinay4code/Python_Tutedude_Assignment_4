import os

print("Current working directory:", os.getcwd())

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:\n")
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = "data_file.txt"
read_file(filename)
