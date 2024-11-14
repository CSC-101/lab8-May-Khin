import sys
# Check if the file name is passed as an argument
if len(sys.argv) != 2:
    print("Error: Please provide a file name.")
    sys.exit(1)

# Try to open the file
try:
    file = open(sys.argv[1], 'r')
    for line in file:
        parts = line.split()
        if len(parts) != 2:
            print(f"Error: Invalid line format: {line.strip()}")
            continue
        try:
            num1 = float(parts[0])
            num2 = float(parts[1])
            print(num1 + num2)
        except ValueError:
            print(f"Error: Could not convert to float: {line.strip()}")

    file.close()

except FileNotFoundError:
    print(f"Error: The file '{sys.argv[1]}' was not found.")
    sys.exit(1)
