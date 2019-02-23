import os, os.path, shutil

def list_dir(path):
    files=[]
    try:
        #list of filenames in directory
        fil = os.listdir(path)
        for f in fil:
            if os.path.isfile(path+'\\'+f):
                files.append(f)
        return(files)
        files.sort(key=lambda s: os.path.getmtime(os.path.join(path, s)))
    except FileNotFoundError:
        print('The specified folder does not exist')
        main()

def calculate_files_per_folder(file_count,max_files_per_folder):
    try:
        files_per_folder = int(file_count/int(max_files_per_folder))
        print(files_per_folder)
        return(files_per_folder)
    except ValueError:
        print('You must specify an integer')
        main()

def create_subfolder(folder_name,suffix,path):
    new_folder = ''
    try:
        new_folder = str(folder_name + '_' + str(suffix))
        os.mkdir(str(path)+'\\'+new_folder)
        print(new_folder)
    except FileExistsError:
        suffix = suffix + 1
        create_subfolder(folder_name,suffix,path)
    return(new_folder)
    print(new_folder)

def size_of_folder(path,folder):
    size = len(os.listdir(path+'\\'+folder))
    return(size)


def move(path,f,new_folder):
    shutil.move(path+'\\'+f, path+'\\'+new_folder+'\\'+f)

def copy(path,f,new_folder):
    shutil.copy2(path+'\\'+f, path+'\\'+new_folder+'\\'+f)


def split_folder_content_in_subfolders(path,max_files_per_folder,op):
    files = list_dir(path)
    #how many files in the directory
    file_count = len(files)
    #how many files must be in each subfolder according to 'max_files_per_folder'
    files_per_folder = calculate_files_per_folder(file_count,max_files_per_folder)
    #original folder name
    folder_name = os.path.basename(path)

    current = 0
    suffix = 1

    while current <= file_count and len(files) > 0:
        new_folder = create_subfolder(folder_name,suffix,path)
        print(new_folder)
        new_folder_size = size_of_folder(path,new_folder)

        while new_folder_size <= int(max_files_per_folder) and len(files) > 0:
            f = files[0]
            if op == 'moved':
                move(path,f,new_folder)
            if op == 'copied':
                copy(path,f,new_folder)
            files.remove(f)

            new_folder_size = size_of_folder(path,new_folder)
            print('Folder size: ' + str(new_folder_size))

            print(str(file_count - len(files)) + " from %s files have been " % int(file_count) + str(op))

        suffix = suffix + 1

def main():
    path = input("Give a path: ")
    max_files_per_folder = input("How many files per folder?: ")
    operacion = input("Do you want to Move or Copy the files to the new subfolders? [M/C]: ")
    if operacion == 'M':
        op = 'moved'
    elif operacion == 'C':
        op = 'copied'
    else:
        print('Option is not valid.')
        operacion = input("Do you want to Move or Copy the files to the new subfolders? [M/C]: ")
    split_folder_content_in_subfolders(path,max_files_per_folder,op)
    print('Completed.')

if __name__ == "__main__":
    main()