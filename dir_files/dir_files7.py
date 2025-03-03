def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("Contents of '", source_file, "' copied to '", destination_file, "' successfully.")
    except FileNotFoundError:
        print("One of the specified files does not exist.")
    except Exception as e:
        print("An error occurred:", str(e))


source_file = r"C:\Users\User\ex2.txt"
destination_file = r"C:\Users\User\ex3.txt"

copy_file(source_file, destination_file)