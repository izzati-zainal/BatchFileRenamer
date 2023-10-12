import os
import sys

commandLineArgs = sys.argv

if len(commandLineArgs) < 3:
    print('Usage: python rename_files.py [directory_path] [pattern]')
    sys.exit()

dir_path = commandLineArgs[1]
pattern = commandLineArgs[2] + "_{{:0{}}}".format(len(str(len(os.listdir(dir_path)))))

# Initialize a counter variable for naming the files
counter = 1

# Get the total number of files in the directory
total_files = len(os.listdir(dir_path))
# Calculate the number of digits for the counter
num_digits = len(str(total_files))

# Iterate over the files in the directory
for filename in os.listdir(dir_path):
    print("Renaming: " + filename + "...")
    
    # Get the file extension
    file_ext = os.path.splitext(filename)[1]
    
    # Create the new file name based on the pattern and counter
    new_filename = pattern.format(counter) + file_ext
    
    # Rename the file with the new file name
    oldFileName = os.path.join(dir_path, filename)
    newFileName = os.path.join(dir_path, new_filename)
    os.rename(oldFileName, newFileName)
    
    # Increment the counter
    counter += 1
    
print("All files renamed.")
