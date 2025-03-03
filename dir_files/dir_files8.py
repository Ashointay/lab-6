import os

def delete_file(path):
    try:
        if os.path.exists(path):
            print("The path '", path, "' exists.")

            if os.access(path, os.F_OK):
                os.remove(path)
                print("File '", path, "' deleted successfully.")
            else:
                print("File '", path, "' is not accessible.")
        else:
            print("The path '", path, "' does not exist.")
    except Exception as e:
        print("An error occurred: ", str(e))

specified_path = r"C:\Users\User\ex3.txt"

delete_file(specified_path)