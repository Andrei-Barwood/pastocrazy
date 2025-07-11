#!/usr/bin/env python3

import os
import sys
import glob
import subprocess

# Directory where the functionality scripts are located
scripts_dir = "scripts"

def show_help():
    """
    Displays the help message with available script options.
    """
    print("Usage: python3 cli.py [option name]")
    print("You can use quotes for names with spaces, e.g., python3 cli.py \"01 - bienvenida\"")
    print("\nAvailable options:")
    print()

    # Find available scripts in the 'scripts' folder and sort them alphabetically
    try:
        scripts = sorted(glob.glob(os.path.join(scripts_dir, "*.py")))
        if not scripts:
            print("No scripts found in the 'scripts' directory.")
        
        for file_path in scripts:
            # Get the filename without the extension
            script_name = os.path.splitext(os.path.basename(file_path))[0]
            print(f"  * {script_name}")

    except FileNotFoundError:
        print(f"❌ Error: The directory '{scripts_dir}' was not found.")

    print("\n  -h, --help")


def main():
    """
    Main function to execute the script based on command-line arguments.
    """
    # Get all arguments after the script name itself
    args = sys.argv[1:]

    # Check if no arguments were provided or if help was requested
    if not args or args[0] in ['-h', '--help']:
        show_help()
        sys.exit(0)

    # MODIFICATION: Join all arguments to form a single option name.
    # This allows for script names with spaces, e.g., `python3 cli.py 01 - powers of ten`
    option = " ".join(args)
    
    # In Python, we will assume the scripts to be executed are also Python scripts (.py)
    script_path = os.path.join(scripts_dir, f"{option}.py")

    # Check if the script exists and execute it
    if os.path.exists(script_path):
        try:
            # MODIFICATION: Use subprocess.run and pass arguments as a list.
            # This is safer than os.system and handles paths with spaces correctly without manual quoting.
            subprocess.run([sys.executable, script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error executing the script: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            sys.exit(1)
    else:
        print(f"❌ Error: The option '{option}' does not exist. Use -h or --help to see available options.")
        sys.exit(1)

if __name__ == "__main__":
    main()