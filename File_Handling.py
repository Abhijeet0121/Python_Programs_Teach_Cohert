with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

#Printing the File
with open("geek.txt", "r") as file:
    content = file.read()
    print(content)

try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()

