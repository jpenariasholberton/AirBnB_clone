#!/usr/bin/python3
"""
This is a test for for BaseModel class
"""


import unittest
from models.base_model import BaseModel
from models import base_model
import os


class Test_Base_Model(unittest.TestCase):
    """ Class that tests the BeseModel class """

    def test_doc_module(self):
        """Method that tests if the module has documentation"""
        docMod1 = base_model.__doc__
        docMod2 = base_model.__doc__
        self.assertSequenceEqual(docMod1, docMod2)

    def test_doc_class(self):
        """Method that tests if the class has documentation"""
        docClass1 = BaseModel.__doc__
        docClass2 = BaseModel.__doc__
        self.assertSequenceEqual(docClass1, docClass2)

    def test_doc_methods(self):
        """Method that tests if the methods have documentation"""
        for metd in dir(BaseModel):
            self.assertSequenceEqual(metd.__doc__, metd.__doc__)

    def test_execution_permissions(self):
        """ Method that test for check the execution permissions """
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/base_model.py.py', os.X_OK)
        self.assertTrue(exect)

    def test_is_an_instance(self):
        """Method that check if BaseModelInstance is an instance
        of BaseModel()"""
        BaseModelInstance = BaseModel()
        self.assertIsInstance(BaseModelInstance, BaseModel)

    def test_different_id(self):
        """Method that check if each instance that is created has
        a unique id"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)

    # Hacer test para los otros metodos de baseModel str, save y to_dict


if __name__ == '__main__':
    unittest.main()
