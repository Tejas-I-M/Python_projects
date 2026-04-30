import os

class Filemanager:
    def __init__(self,base_path = r"C:\Users\Tejas\Desktop\Python_projects\Day-09_FileSystem\files"):
        self.base_path = base_path

        if not os.path.exists(base_path):
            os.makedirs(base_path)
    def create_file(self,file_name,content):
        path = os.path.join(self.base_path,file_name)

        if os.path.exists(path):
            print("file already created")
            return
        with open(path,"w") as f:
            f.write(content)
        print(f"File name {file_name} created successfully")
    def read_file(self,file_name):
        path = os.path.join(self.base_path,file_name)
        if not os.path.exists(path):
            print(f"No file named {file_name} exists")
            return
        with open(path,"r") as f:
            print("\n Content: \n",f.read())
    def delete_file(self,file_name):
        path = os.path.join(self.base_path,file_name)
        if not os.path.exists(path):
            print(f"no file named {file_name} exists.")
            return
        os.remove(path)
        print(f"file {file_name} deleted successfully!")
    def list_files(self):
        files = os.listdir(self.base_path)
        if not files:
            print("no files exists")
            return 
        for file in files:
            print(f"-{file}")
fm = Filemanager()

while True:
    print("\n1.create 2.read 3.list 4.delete 5.exit")
    choice = input("Enter your option(1-5): ")
    if choice == "1":
        name = input("enter file name: ")
        content = input("enter the content: ")
        fm.create_file(name,content)
    elif choice == "2":
        name = input("enter file name: ")
        fm.read_file(name)
    elif choice == "3":
        fm.list_files()
    elif choice =="4":
        name = input("enter the file name: ")
        fm.delete_file(name)
    elif choice == "5":
        break
    else:
        print("invalid option!!")
    