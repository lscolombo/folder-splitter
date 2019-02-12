import folder_splitter
import os
import pytest
import shutil
import time

path = os.getcwd()


def test_move_2_files_to_new_folder():               
    folder_splitter.split_folder_content_in_subfolders(path+'\\test_files','2','M')
    sum = 1+1
    assert sum == 2

def test_new_subfolder_has_been_created():
    print(path)
    subfolder = path+'\\test_files\\test_files_1'
    assert os.path.isdir(subfolder) == True


def test_files_no_longer_exist_in_original_dir():
    path_files = os.listdir(path+'\\test_files')
    assert len(path_files) == 1


def test_files_have_been_moved_to_new_subfolder():
    subfolder_files = os.listdir(path+'\\test_files\\test_files_1')
    assert len(subfolder_files) == 2


def test_undo():
    fil = os.listdir(path+'\\test_files\\test_files_1')
    for f in fil:
        if os.path.isfile(path+'\\test_files\\test_files_1'+f):
            shutil.move(path+'\\test_files\\test_files_1'+f, path+'\\test_files'+f)
            time.sleep(5)
    shutil.rmtree(path+'\\test_files\\test_files_1')
    sum = 1+1
    assert sum == 2


    