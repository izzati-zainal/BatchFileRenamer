# Batch File Renaming Script with Leading Zeros

This Python script allows you to batch rename files in a specified directory, adding leading zeros to the counter in the new file names. 

## Description

When you have a set of files that you want to rename sequentially, such as renaming images or documents, this script can help you accomplish that task efficiently. The script takes a user-defined pattern and renames the files in the specified directory with names like "filename_001", "filename_002", "filename_003", and so on, ensuring that the counterpart has leading zeros to maintain a consistent file name format.

## How to Use

1. **Clone or Download**: Clone or download this repository to your local machine.

2. **Install Python**: Ensure you have Python installed on your system.

3. **Navigate to Script Directory**: Open a command prompt or terminal and navigate to the directory where the Python script ('batch-rename-leading-0.py') is located. For example, if the script is located at 'c:\temp'

   **Example:**

   ```bash
   cd c:\temp

4. Execute the script with the following command, replacing [directory_path] with the directory containing your files and [pattern] with your desired pattern for the new filenames.

   ```bash
   python rename_files.py [directory_path] [pattern]

  For example, if you want your files located at 'c:\image' to be named as "image_001," "image_002," etc., you would run:

   ```bash
   python batch-rename-leading-0.py "c:\myimage" image

5. The script will process the files in the specified directory and rename them according to the pattern, adding leading zeros as needed.
6. After the script completes, you'll receive a message confirming that all files have been successfully renamed.

