new_file = open('New_File.txt', 'x')
new_file.close()

import os
print("Checking for new File exist or not.....")
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
else:
    print("the File does not exists")
          

my_file = open("New_File.txt", "w")
my_file.write("Hi! i am praise")
my_file.close()
os.remove('Codingal.txt')
os.rmdir('Folder')