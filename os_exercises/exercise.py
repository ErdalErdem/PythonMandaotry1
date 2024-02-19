import os

# Step 1
folder_path = 'os_exercises/exercises'
os.makedirs(folder_path, exist_ok=True)

# Step 2 and 3: 
file_path1 = os.path.join(folder_path, 'exercise.py')
with open(file_path1, 'w') as file:
    file.write("print('Hello, World!')")  

# Step 4
file_path2 = os.path.join(folder_path, 'exercise2.py')
with open(file_path2, 'w') as file:
    file.write("print('Another Hello, World!')")  

# Step 5
def read_and_print_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

content1 = read_and_print_file_content(file_path1)
content2 = read_and_print_file_content(file_path2)

content1, content2