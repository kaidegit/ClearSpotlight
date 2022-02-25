import os


def clear_file(dir):
    file_list = []
    dir_list = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            file = {
                "root": root,
                "name": name
            }
            file_list.append(file)
            # print(os.path.join())
            # if (re.)
        for name in dirs:
            dir = {
                "root": root,
                "name": name
            }
            dir_list.append(dir)
    
    for file in file_list:
        temp_file = file.copy()
        temp_file["name"] = "._" + temp_file["name"]
        if temp_file in file_list:
            # print(temp_file)
            file_list.remove(temp_file)
            file_to_del = os.path.join(temp_file["root"], temp_file["name"])
            print(file_to_del)
            os.remove(file_to_del)
    
    for dir in dir_list:
        temp_file = dir.copy()
        temp_file["name"] = "._" + temp_file["name"]
        if temp_file in file_list:
            # print(temp_file)
            file_list.remove(temp_file)
            file_to_del = os.path.join(temp_file["root"], temp_file["name"])
            print(file_to_del)
            os.remove(file_to_del)
    
    for file in file_list:
        if file["name"] == ".DS_Store":
            file_to_del = os.path.join(file["root"], file["name"])
            print(file_to_del)
            os.remove(file_to_del)


dir_to_clean = [
    "E:\MCUResource",
]
for each in dir_to_clean:
    clear_file(each)
