"""
MIT License

Copyright (c) 2024 Darshan P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This script calculates the percentage of the current day that has elapsed and 
displays it as a progress bar in the console.
"""

"""
This module provides tools to backup and create new rotor configurations for an Enigma-like encryption system.
It includes functionality for backing up current rotor settings and generating new rotor configurations.
"""

import random
import os
import shutil
from datetime import datetime

def randmatch():
    """
    Generates a random mapping of ASCII characters in the range 33 to 125, used to simulate the wiring of an Enigma rotor.

    Returns:
        dict: A dictionary where keys and values are ASCII characters in a shuffled and reversed mapping.
    """
    lst = [chr(a) for a in range(33, 126)]
    random.shuffle(lst)
    return dict(zip(lst, lst[::-1]))

def backup_default_rotor():
    """
    Backs up the 'defaultRotor.py' file from a relative path within the project to a backup directory in the user's home folder.
    The backup is timestamped to allow multiple versions to be stored.
    """
    # Get the current script directory
    script_dir = os.path.dirname(__file__)

    # Define source and destination paths using relative paths
    source_path = os.path.join(script_dir, "..", "enigmacifra", "defaultRotor.py")
    backup_folder = os.path.join(os.path.expanduser("~"), ".enigmabackup")
    backup_path = os.path.join(backup_folder, f"{os.path.basename(source_path)}_{datetime.now().strftime('%Y%m%d%H%M%S')}.backup")

    # Ensure the backup folder exists
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Copy the file to the backup location
    shutil.copy(source_path, backup_path)

    print(f"Backup of defaultRotor.py saved as: {backup_path}")

def create_rotors(count):
    """
    Creates a specified number of new rotor configurations and writes them to the 'defaultRotor.py' file.

    Args:
        count (int): The number of new rotor configurations to create.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "defaultRotor.py")
    rotors = [randmatch() for _ in range(count)]
    with open(file_path, "w") as f:
        f.write("ROTORS = ")
        f.write(repr(rotors))
        f.write("\n")
    print(f"New rotors created and saved in: {file_path}")

if __name__ == "__main__":
    # The main section prompts the user to back up the current rotors before potentially creating new ones.
    rotor_file = "defaultRotor.py"
    backup_default_rotor()
    # Optionally, create new rotors. Uncomment the next line and specify the count to activate this feature.
    # create_rotors(count)
