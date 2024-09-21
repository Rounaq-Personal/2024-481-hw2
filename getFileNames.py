import os

def list_files_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return []

    # Get the list of files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    return files

# Assume rk_path is defined somewhere in your code
rk_path = "/YOUR/TEST_SUITE/FILEPATH/HERE"  # Replace this with your actual path

# Get the list of files
file_list = list_files_in_folder(rk_path)

# Print the list of files
if file_list:
    print("Files in the folder:")
    for file in file_list:
        print(file)
else:
    print("No files found in the folder.")
