def modify_file_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = modify_file_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: File could not be read or written.")

if __name__ == "__main__":
    main()
