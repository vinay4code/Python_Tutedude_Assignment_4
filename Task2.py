def write_to_file(filename):
    data = input("Enter some data to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')
    print("Initial data written.")

def append_to_file(filename):
    extra_data = input("Enter additional data to append to the file: ")
    with open(filename, 'a') as file:
        file.write(extra_data + '\n')
    print("Additional data appended.")

def read_file(filename):
    print("\nFinal file content:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = "output.txt"
write_to_file(filename)
append_to_file(filename)
read_file(filename)