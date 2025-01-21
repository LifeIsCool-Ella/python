import datetime
import os
#print(os.getcwd())
#os.chdir("rpa_basic")
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())
#os.chdir("../..")
#print(os.getcwd())
#os.chdir("c:/")
#print(os.getcwd())

#file_path = os.path.join(os.getcwd(), "my_file.txt")
#print(file_path)
#open(file_path) as f

#print(os.path.dirname(r"C:\dev\git\python\python5\rpa_basic\2_desktop\my_file.txt"))

file_path2 = os.path.join(os.getcwd(), "11_file_system.py")
ctime = os.path.getctime(file_path2)
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

mtime = os.path.getmtime("11_file_system.py")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

atime = os.path.getmtime("11_file_system.py")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

size = os.path.getsize(file_path2)
print(size)

