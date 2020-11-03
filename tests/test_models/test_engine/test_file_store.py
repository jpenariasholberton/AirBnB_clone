#!/usr/bin/python3
"""
This is a test for FileStorage module
"""

import unittest
from models.engine.file_storage import FileStorage
from models.engine import file_storage
import os


class Test_fileStorage(unittest.TestCase):
    """ Class that tests the fileStorage class """

    def test_doc_module(self):
        """Method that tests if the module has documentation"""
        docMod1 = file_storage.__doc__
        docMod2 = file_storage.__doc__
        self.assertSequenceEqual(docMod1, docMod2)

    def test_doc_class(self):
        """Method that tests if the class has documentation"""
        docClass1 = FileStorage.__doc__
        docClass2 = FileStorage.__doc__
        self.assertSequenceEqual(docClass1, docClass2)

    def test_doc_methods(self):
        """Method that tests if the methods have documentation"""
        for metd in dir(FileStorage):
            self.assertSequenceEqual(metd.__doc__, metd.__doc__)

    def test_execution_permissions(self):
        """ Method that test for check the execution permissions """
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if fileStorageInstance is an instance
        of FileStorage()"""
        fileStorageInstance = FileStorage()
        self.assertIsInstance(fileStorageInstance, FileStorage)

if __name__ == '__main__':
    unittest.main()
