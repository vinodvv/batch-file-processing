import os
from datetime import datetime

# Directory containing the files to be processed
directory = 'files'

# Get a list of all filenames in the directory
filenames = os.listdir(directory)

for filename in filenames:
    # Create the full path to the file
    filepath = os.path.join(directory, filename)

    # Open the file and read its content
    with open(filepath, 'r') as file:
        content = file.read()

        # Split the content into words and count them
        words = content.split()
        word_count = len(words)

    # Get the current day of the week
    day = datetime.now().strftime("%A")

    # Create a new filename based on the word count and the current day
    new_filename = f"{filename[:-4]}-{word_count}-{day}.txt"

    # Create the new file path and rename the file
    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    print(f"Renamed {filename} to {new_filename}!")
    
print("File renaming successfully completed!")
