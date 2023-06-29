def add_period_to_lines(filename):
    with open(filename, 'r+') as file:
        lines = file.readlines()  # Read all lines from the file
        file.seek(0)  # Move the file pointer to the beginning
        file.truncate()  # Clear the file content

        for line in lines:
            line = line.rstrip('\n')  # Remove newline character
            line += '.'  # Add a period at the end
            file.write(line + '\n')  # Write the modified line back to the file

    print(f"Period added to each line in '{filename}'.")


# Example usage
file_path = 'random_text.txt'  # Update with your file path
add_period_to_lines(file_path)
