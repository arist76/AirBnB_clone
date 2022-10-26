#!/usr/bin/env python3
"""
Contains test for base model in models.base_model
"""
from models.base_model import BaseModel
import unittest
import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test for base_model

    a comprehensive test for base_model and all of its methods

    Attributes
    ----------
    my_model : BaseModel
        the base model created automatically object to be tested

    my_model : BaseModel
        the base model deserialized from a valid dict
    """

    def setUp(self):
        """
        Creates the my_model and my_model2 instance attribute
        """
        self.my_model = BaseModel()
        model_dict = self.my_model.to_dict()
        self.my_model2 = BaseModel(**model_dict)

    def test_init(self):
        """
        Tests the initialization of BaseModel object

        it tests if:
            1 - the id is a valid UUID
            2 - created_at and updated_at are datetime objects
            3 - created_at and updated_at are equal
            4 - does all of the above for the second model
        """
        self.assertIsInstance(uuid.UUID(self.my_model.id), uuid.UUID)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertEqual(self.my_model.created_at, self.my_model.updated_at)

        # tests for my_model2
        self.assertIsInstance(self.my_model2, BaseModel)
        self.assertIsInstance(uuid.UUID(self.my_model2.id), uuid.UUID)
        self.assertIsInstance(self.my_model2.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model2.updated_at, datetime.datetime)

    def test_str(self):
        """
        Tests __str__ of the BaseModel object

        it tests if:
            1 - str returns the valid string format
        """
        self.assertEqual(
            str(self.my_model),
            f"[BaseModel] ({self.my_model.id}) {self.my_model.__dict__}",
        )

    def test_save(self):
        """
        Tests the save method of the Basemodel object

        it tests if:
            1 - created_at equals updated_at
            2 - updated_at is updated no save and
                updated_at is greater than created_at
        """
        before_save = self.my_model.updated_at
        self.assertEqual(before_save, self.my_model.created_at)
        self.my_model.save()
        after_save = self.my_model.updated_at
        self.assertGreaterEqual(after_save, before_save)

    def test_to_dict(self):
        """
        Tests to_dict method of BaseModel object

        it tests if:
            1 - the dict has __class__ key with value BaseModel
            2 - created_at and updated_at are valid isoformat strings
            3 - it stores instance attributes
        """
        d = self.my_model.to_dict()
        self.assertIsInstance(d, dict)

        self.my_model.test_str1 = "Hell0 world!!!"
        self.my_model.test_str2 = "This is A base Model"
        d = self.my_model.to_dict()

        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(
            datetime.datetime.fromisoformat(d["created_at"]), datetime.datetime
        )
        self.assertIsInstance(
            datetime.datetime.fromisoformat(d["updated_at"]), datetime.datetime
        )
        self.assertEqual(d["test_str1"], "Hell0 world!!!")
        self.assertEqual(d["test_str2"], "This is A base Model")


if __name__ == "__main__":
    unittest.main()
