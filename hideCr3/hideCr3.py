#Hides all .cr3 file so that they do not bother me when i'm looking at my camera pictures.

import os
import ctypes

# Function to set file as hidden in Windows
def set_hidden(file_path):
    FILE_ATTRIBUTE_HIDDEN = 0x02
    
    ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN) #this is kinda complicated, it can be done with subprocess instead
    if not ret:  # There was an error
        raise ctypes.WinError()

# Directory of the script
directory = os.path.dirname(os.path.realpath(__file__))

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".cr3"):
        file_path = os.path.join(directory, filename)
        try:
            set_hidden(file_path)
            print(f"File {filename} is now hidden.")
        except Exception as e:
            print(f"Error hiding file {filename}: {e}")

