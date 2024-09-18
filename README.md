# Batch File Processing Project

This Python project processes a batch of text files in a specified directory. It reads the content of each file, counts the number of words, and renames the file to include the word count and the current day of the week.

## Features

- Automatically renames files based on their word count.
- Appends the current day of the week to the filename.
- Processes all `.txt` files in the specified directory.

## How It Works

The script performs the following actions for each file in the `files` directory:
1. Reads the content of the file.
2. Counts the number of words in the file.
3. Gets the current day of the week (e.g., Monday, Tuesday).
4. Renames the file to follow this format: `<original_filename>-<word_count>-<day_of_week>.txt`.
5. Prints a message for each file that is successfully renamed.

### Example

If the script processes a file named `example.txt` containing 100 words on a Monday, the file will be renamed to `example-100-Monday.txt`.

## Prerequisites

- Python 3.x
- Basic knowledge of Python and file handling

## Installation

1. Clone this repository or download the script.
2. Ensure Python is installed on your machine.
3. Place the text files to be processed inside a folder named `files` in the same directory as the script.

## Usage

1. Open the terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python add_day_and_word_count_to_filenames.py
   