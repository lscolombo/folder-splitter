import folder_splitter
import os
import pytest
import shutil
import time
import pyfakefs as fs

import unittest
from unittest.mock import patch

class FolderSplitterMethods(unittest.TestCase):

    # @mock.patch('folder_splitter.os.mkdir')
    def test_new_subfolder_has_been_created(self):
        with patch('folder_splitter.create_subfolder') as mocked_create_subfolder:
            mocked_create_subfolder.return_value = 'folder_1'        
            result=mocked_create_subfolder('folder',1,'\\path\\folder')
            self.assertEqual(result,'folder_1')

    def test_file_no_longer_exists_in_original_dir(self):
        with patch('folder_splitter.move') as mocked_move:
            with patch('folder_splitter.os.listdir') as mocked_listdir:
                mocked_move('\\path\\folder','file','folder_1')
                file_list = mocked_listdir('\\path\\folder\\folder_1')
                self.assertEqual(len(file_list),0)
            
if __name__ == '__main__':
    unittest.main()


# path = os.getcwd()
# def test_move_2_files_to_new_folder(fs):               
# def test_new_subfolder_has_been_created(fs):
# def test_files_have_been_moved_to_new_subfolder():

    