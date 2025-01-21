import datetime
import os

print(os.listdir())
#print(os.listdir("rpa_basic"))

result = os.walk(".")
print(result)

for root, dirs, files in result:
    print(root, dirs, files)

name = "11_file_system2.py"
result = []
for root, dirs, files in os.walk("."):
    if name in files:
        result.append(os.path.join(root, name))

print(result)

import fnmatch
pattern = "*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))

print(result)

print(os.path.isdir("rpa_basic"))
print(os.path.isfile("rpa_basic"))

print(os.path.isdir("run_btn.png"))
print(os.path.isfile("run_btn.png"))

if os.path.exists("rpa_basic"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("존재하지 않습니다.")

open("new_file.txt", "a").close()

#os.rename("new_file.txt", "new_file_rename.txt")

#os.remove("new_file_rename.txt")


#os.mkdir("new_folder")

#os.mkdir("new_folders/a/b/c")

#os.makedirs("new_folders/a/b/c")

#os.rename("new_folder", "new_folder_rename")

#os.rmdir("new_folder_rename")

import shutil
#shutil.rmtree("new_folders")

shutil.copy("my_file.txt", "test_folder")
shutil.copy("my_file.txt", "test_folder/copied_my_file.txt")

shutil.copyfile("my_file.txt", "test_folder/copied_my_file_2.txt")
shutil.copy2("my_file.txt", "test_folder/copied_my_file_3.txt")

shutil.copytree("test_folder", "test_folder2")
shutil.copytree("test_folder", "test_folder3")

shutil.move("test_folder", "test_folder3")
