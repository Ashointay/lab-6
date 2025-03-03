import os 
def check(path): 
    if os.path.exists(path): 
        print("path exists") 
        if os.access(path, os.R_OK): 
            print("readable")
        else: 
            print("not readable") 
        if os.access(path, os.W_OK):
            print("writable") 
        else: 
            print("not writable") 
        if os.access(path, os.X_OK):
            print("executable") 
        else: 
            print("not executable") 
    else: 
        print("path doesn't exist") 

path = r"C:\Users\User"
check(path)
