import os

# Specify the directory where the files are located
directory = 'files'

# Get a list of all filenames in the specified directory
filenames = os.listdir(directory)

# Loop through each file in the directory
for filename in filenames:
    # Construct the full file path
    filepath = os.path.join(directory, filename)

    # Modify the current filename by removing current date
    new_filename = f"{filename[0]}.txt"

    # Construct the new full file path with updated filename
    new_filepath = os.path.join(directory, new_filename)

    # Rename the original file to the new filename
    os.rename(filepath, new_filepath)

    # Print a message indicating the renaming of the file
    print(f"Renamed '{filename}' to '{new_filename}'")

# Print a message indicating the renaming of the file
print("File renaming completed!")
