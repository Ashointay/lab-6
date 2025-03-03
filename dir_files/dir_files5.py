def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("Data has been written to '", filename, "' successfully.")
    except Exception as e:
        print("An error occurred: ", str(e))


filename = r"C:\Users\User\ex2.txt"


data_list = ['apple', 'banana', 'orange', 'grape']

write_list_to_file(filename, data_list)