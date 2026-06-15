#Reading files:
# with open("my_file.txt") as file:
#     contents = file.read()

#Writing to files:
with open("new_file.txt", mode="w") as file:
    contents = file.write("New text.")