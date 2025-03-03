import os

def analyze_path(path):
    if os.path.exists(path):
        print("The path '", path, "' exists.")
        directory_name, file_name = os.path.split(path)
        print("Directory: ", directory_name)
        print("Filename: ", file_name)
    else:
        print("The path '", path, "' does not exist.")

specified_path = r"C:\Users\User"

analyze_path(specified_path)
