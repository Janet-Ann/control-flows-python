try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file was not found. Please check the file path and try again.")
