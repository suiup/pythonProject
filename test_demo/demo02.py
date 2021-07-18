
filename = "f1.txt"
def modify_name():
    global filename
    print("local filename: ", filename)
    filename = "f2.txt"
    print("local filename: ", filename)

modify_name()
print("global filename: ", filename)