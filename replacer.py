import os
import shutil

# Path to the original cs2_video.txt file
source_file = r'cs2_video.txt'

# Base path to the Steam userdata directory
steam_userdata_path = r'C:\Program Files (x86)\Steam\userdata'

# Directory structure after the account ID
target_subpath = r'730\local\cfg\cs2_video.txt'

def replace_cs2_video_file(source_file, steam_userdata_path, target_subpath):
    # Check if the source file exists
    if not os.path.isfile(source_file):
        print(f"Source file not found: {source_file}")
        return

    # Iterate over each folder (account ID) in the userdata directory
    for account_id in os.listdir(steam_userdata_path):
        account_path = os.path.join(steam_userdata_path, account_id)
        if os.path.isdir(account_path):
            target_path = os.path.join(account_path, target_subpath)

            # Check if the target path exists
            if os.path.isfile(target_path):
                try:
                    # Copy the source file to the target location, replacing the old file
                    shutil.copy2(source_file, target_path)
                    print(f"Replaced {target_path}")
                except Exception as e:
                    print(f"Failed to replace {target_path}: {e}")
            else:
                print(f"Target file not found: {target_path}")

# Execute the function
replace_cs2_video_file(source_file, steam_userdata_path, target_subpath)
print()
input("Press enter to exit...")