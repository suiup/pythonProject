class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def change_name(self, new_name):
        self.name = new_name

my_file = File("my_file")

my_file.change_name("new_name")
print(my_file.name)

