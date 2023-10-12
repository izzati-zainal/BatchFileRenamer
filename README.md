# Batch File Renaming Script with Leading Zeros

This Python script allows you to batch rename files in a specified directory, adding leading zeros to the counter in the new file names. 

## Description

When you have a set of files that you want to rename sequentially, such as renaming images or documents, this script can help you accomplish that task efficiently. The script takes a user-defined pattern and renames the files in the specified directory with names like "filename_001", "filename_002", "filename_003", and so on, ensuring that the counterpart has leading zeros to maintain a consistent file name format.

## How to Use

1. **Clone or Download**: Clone or download this repository to your local machine.

2. **Install Python**: Ensure you have Python installed on your system.

3. **Navigate to Script Directory**: Open a command prompt or terminal and navigate to the directory where the script is located. For example, if your batch file is located at "c:\temp\myfile", and "myfile" is the name of the folder that contains the batch files, you should navigate to the directory "c:\temp". Make sure the Python script (`batch-rename-leading-0.py`) is in that same directory.

   **Example:**

   '''bash
   cd c:\temp

4. Execute the script with the following command, replacing [pattern] with your desired pattern for the new filenames. For example, if you want your files to be named as "image_001," "image_002," etc., you would run:
   
   python batch-rename-leading-0.py "image_"

5. The script will process the files in the specified directory and rename them according to the pattern, adding leading zeros as needed.

6. After the script completes, you'll receive a message confirming that all files have been successfully renamed.


