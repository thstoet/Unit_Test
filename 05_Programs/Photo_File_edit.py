import os
import shutil

def edit_file():
    path_1 = os.path.join("C:\Python\Script_me\Programme\import_raw")
    path_2 = os.path.join("C:\Python\Script_me\Programme\import_edit")
    bad_char = "-"
    right_char = "_"
    photo_files_raw = os.listdir(path_1)    # listdir gibt Liste an Files zurück, welche sich im Ordner befinden
    photo_files_edit = os.listdir(path_2)

    print("First Check")
    if (os.path.exists(path_1) == True) and (os.path.isdir(path_1) == True) and \
            (os.path.exists(path_2) == True) and (os.path.isdir(path_2) == True):
        print("First Check Okay")
    else:
        print("Hier stimmt was nicht. Check mal die Ordner")
        return

    L1 = []
    L2 = []

    for file_name in photo_files_raw:
        L1.append(file_name)

    for file_name in L1:
        L2.append(file_name.replace(bad_char, right_char, 1))

    index = 0
    while index < len(L1):
        source = path_1 + "\\" + L1[index]
        target = path_2 + "\\" + L2[index]

        shutil.copy(source, target)
        index += 1
    print("Edit erfolgreich!!!")

if __name__ == "__main__":

    while True:
        eingabe = input("Kanns losgehen?(j/n)")
        if eingabe == "j" and "J":
            edit_file()
        else:
            break
    print("FIN")