import os

# Directory containing the files to be processed
directory = 'files'

# Get a list of all filenames in the directory
filenames = os.listdir(directory)

for filename in filenames:
    # Create the full path to the file
    filepath = os.path.join(directory, filename)

    # Create new file name by removing day and word count from the filename
    new_filename = f"{filename[0]}.txt"

    # Create the new file path and rename the file
    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    print(f"Renamed {filename} to {new_filename}")

print("File renaming process completed!")
