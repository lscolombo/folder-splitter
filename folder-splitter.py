import os, os.path, shutil
import shutil

def split_folder_content_in_subfolders(path,max_files_per_folder):
    files=[]
    try:
        #list of filenames in directory
        files = os.listdir(path)
    except FileNotFoundError:
        print('The specified folder does not exist')
        main()
    #how many files in the directory
    file_count = len(files)
    #how many files must be in each subfolder according to 'max_files_per_folder'
    try:
        files_per_folder = int(file_count/int(max_files_per_folder))
        print(files_per_folder)
    except ValueError:
        print('You must specify an integer')
        main()

    #original folder name
    folder_name = os.path.basename(path)

    current = 0
    suffix = 1

    while current <= file_count:
        new_folder = str(folder_name + '_' + str(suffix))
        os.mkdir(str(path)+'\\'+new_folder)
        new_folder_size = len(os.listdir(path+'\\'+new_folder))

        while new_folder_size <= int(max_files_per_folder):
            f = files[current]
            #os.rename(path+'\\'+f, new_folder+'\\'+f)
            shutil.move(path+'\\'+f, path+'\\'+new_folder+'\\'+f)
            files.remove(f)

            new_folder_size = len(os.listdir(path+'\\'+new_folder))
            current = current + 1

            print(str(current + 1) + " from %s files have been moved" % int(file_count))

        suffix = suffix + 1

def main():
    path = input("Give a path: ")
    max_files_per_folder = input("How many files per folder?: ")
    split_folder_content_in_subfolders(path,max_files_per_folder)

if __name__ == "__main__":
    main()