import os

import subprocess

def create_executable(script_path, output_dir, additional_folders-None):

if not os.path.isfile(script_path):

print(f"Script not found: {script_path}")

return

# Base PyInstaller command

command - [

"pyinstaller",

"--onefile", # Single executable

"--noconsole", # No console window (for GUI apps, optional)

f"--distpath=(output_dir}", # Specify output directory

script_path, #Path to the main script

#Add additional folders as data
]
if additional_folders:

for folder in additional_folders:

if os.path.isdir(folder):

command.append(f"--add-data-{folder}{os.pathsep}{folder}")

else:

print(f"Folder not found: (folder)")

#Run the PyInstaller command

try:

subprocess.run(command, check-True)

print(f"Executable created successfully in (output_dir}")

except subprocess.CalledProcessError as e:

print(f"Error occurred: {e}")

# Usage

script path = "invoice_automation.py" # Path to your main Python script

output_dir = "output" # Directory for the executable

additional_folders = ["Invoice_Automation"]

# Folders to include

create_executable(script_path, output_dir, additional_folders
