# Open a file in read mode
with open("example.txt", "r") as file:
        content = file.read()
        print(content)

with open("output.txt", "r") as file:
        content = file.write("I love the woman im becoming")
        print(content)