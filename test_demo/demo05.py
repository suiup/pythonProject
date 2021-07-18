import os

print("当前目录： ", os.getcwd())
print("current content: ", os.listdir())

print("current folder: ", os.getcwd())

# 在当前文件夹创建文件夹  判断是否含有了这个文件
os.makedirs("project", exist_ok=True)
print(os.path.exists("project"))






