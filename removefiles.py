import time, os, shutil

path = input("Input path to clean:")
days = input("Input amount of days a file can exist for:")

seconds = int(days) * 86400
#print(int(time.time()))

if os.path.exists(path):
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            if int(time.time()) - seconds > ctime:
                os.remove(path)
                print = True
            else: print("File is within time range.")
        for name in dirs:
            os.path.join(root, name)
            ctime2 = os.stat(path).st_ctime
            if int(time.time()) - seconds > ctime:
                shutil.rmtree(path)
                print2 = True
            else: print("Folder is within time range.")
    if print == True:
        print("Files have been deleted.")
    if print2 == True:
        print("Folders have been deleted.")
else:
    print("Please enter a valid path.")
    time.sleep(2)
    quit()