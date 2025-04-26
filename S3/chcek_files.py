import os

local_folder = r"D:\projects\BL_DE_Digit Insurance\PostgressSQL\data"

print("📂 Listing all files found:")
for root, dirs, files in os.walk(local_folder):
    for file in files:
        print(os.path.join(root, file))