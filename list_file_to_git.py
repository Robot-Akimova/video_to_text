import os

directory = 'D:\code\datashcool'

files = os.listdir(directory)
files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
print(files)