import os
current_dir = os.getcwd()

for filename in os.listdir(current_dir):
    file_path = os.path.join(current_dir, filename)

    if os.path.isfile(file_path) and not filename.endswith(".pdf"):
        new_name = filename + ".pdf"
        new_path = os.path.join(current_dir, new_name)

        os.rename(file_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("Done!")