import os
from datetime import datetime

# Specify the directory where the files are located
directory = 'files'

# Get a list of all filenames in the specified directory
filenames = os.listdir(directory)

# Loop through each file in the directory
for filename in filenames:
    # Construct the full file path
    filepath = os.path.join(directory, filename)

    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Modify the current filename to include the current date
    new_filename = f"{filename[:-4]}-{current_date}.txt"

    # Construct the new full file path with the updated filename
    new_filepath = os.path.join(directory, new_filename)

    # Rename the original file to the new filename
    os.rename(filepath, new_filepath)

    # Print a message indicating the renaming of the file
    print(f"Renamed '{filename}' to '{new_filename}'")

# Print a message when the file renaming process is completed
print('File renaming completed!')
