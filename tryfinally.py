try:
    file = open('example.txt', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("The file was not found. ")
finally:
    file.close()
    print("File closed.")