"""
This module provides functions to open files and directories from a path stored in the clipboard.

It uses the pyperclip module to access the clipboard and subprocess to open the file explorer.
"""
import os
import sys
import subprocess
import pyperclip


def open_clipboard():
    """
    Opens the file or folder path stored in the clipboard.

    This function checks if the path exists. If not, it prompts the user to
    create it. If the path is a file, it updates the path to its parent directory.
    Finally, it opens the file or folder in the default file explorer.

    Raises:
        PathFormatError: If the path does not exist and user chooses not to create it,
        or if the path is expected to be a folder but is a file.
    """
    path = pyperclip.paste()  # Get the path from the clipboard

    if not os.path.exists(path):
        print('Error: File or folder does not exist.')
        if input('Do you want to create it? (y/n): ').lower() != 'y':
            raise PathFormatError("User chose not to create the path.")

        if "." in os.path.basename(path) and not confirm_is_folder():
            raise PathFormatError(
                "Provided path is a file but a folder path was expected.")

        create_directory(path)

    if os.path.isfile(path):
        path = os.path.dirname(path)

    open_in_explorer(path)


class PathFormatError(Exception):
    """Exception raised for errors in the input path format."""

    def __init__(self, message="Path is not a valid file or folder path."):
        self.message = message
        super().__init__(self.message)


def confirm_is_folder():
    """Ask the user to confirm if the path is indeed a folder."""
    response = input('Is this path a folder? (y/n): ')
    if response.lower() == 'n':
        sys.exit(1)
    return response.lower() == 'y'


def create_directory(path):
    """Create a directory at the specified path."""
    try:
        os.makedirs(path)
    except OSError as e:
        print(f'Error: Failed to create directory. {e}')
        sys.exit(1)


def open_in_explorer(path):
    """Open the given path in the system's default file explorer."""
    subprocess.Popen(['explorer', path])


if __name__ == '__main__':
    open_clipboard()
    sys.exit(0)
