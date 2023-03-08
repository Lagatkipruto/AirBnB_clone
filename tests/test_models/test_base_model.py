#!/usr/bin/python3
"""Unittesting the base class"""
import unittest
from models.base_model import BaseModel
import os
import datetime
import uuid


class TestBaseModel(unittest.testcase):
    def test_if_BaseModel_instance_has_id(self):
        """tests if the base model has an id at init"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_str_representation(self):
        """tests the string representation for appropriateness"""
        b = BaseModel()
        self.assertEqual(str(b)), "[BaseModel] ({}) {}".format(b.id, b.__dict))

    def test_ids_is_unique(self):
        """tests if the ids are unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id_is_str(self):
        """tests that the idis a str object"""
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_created_at_is_datetime(self):
        """tests that created_at is datetime"""
        b = BaseModel()
        self.assertTrue(b.crated_at) is datetime

    def test_updated_at_is_datetime(self):
        """tests that updates_at is datetime"""
        b= BaseModel()
        self.assertTrue(b.updated_at) is datetime

    def test_two_models_different_created_at(self):
        """tests that two models have different created_ats"""
        b1 = BaseModel
        (sleep 0.05)
        b2 = Basemodel
        selfassertLess(b1.created_at, b2.creatd_at)

    def test_two_models_different_updated_at(self):
        """tests that two models have different updated_at"""
        b1 = BaseModel
        (sleep 0.05)
        b2 = BaseModel
        selfassertLess(b1.updated_at, b2.Updated_at)

    def test_args_unused(self):
        """tests that args is not used"""
        b = BaseModel(None)
        selfAssertNotIn(None, b.__dict__.values())

    def test_that_created_at_equals_updated_at_initially(self):
        """tests  that created_at == updated_at initially"""
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)
        
    def test_that_save_func_update_update_at_attr(self):
        """tests that the save() updates the updated_at"""
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(b.updated_at.microsecond,
                           b.created_at.microsecond)

    def test_if_to_dict_returns_dict(self):
        """tests that BaseModel.to_dict returns dict object"""
        b = BaseModel()
        self.assertTrue(type(b.to_dict()) is dict)

    def test_if_to_dict_returns_class_dunder_method(self):
        """tests that BaseModel.to_dict contains __class__"""
        b = BaseModel()
        self.assertTrue("__class__" in b.to_dict())

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """tests that created_at returned by to_dict is iso string"""
        b = BaseModel()
        self.assertEqual(b.to_dict()["created_at"], b.created_at.isoformat())
    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):

        """tests if updated_at returned by to_ict is iso string"""
        b = BaseModel()
        self.assertEqual(b.to_dict()["updated_at"], b.updated_at.isoformat())

    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """
        Checks that to_dict() returns the expected number of keys/values
        """
        b = BaseModel()
        partial_expectation = {k: v for k, v in b.__dict__.items()
                               if not k.startswith("_")}
        self.assertEqual(len(b.to_dict()), len(partial_expectation) + 1)

    def test_when_kwargs_passed_is_empty(self):
        """
        Checks that id, created_at and updated_at are automatically
        generated if they're not in kwargs
        """
        my_dict = {}
        b = BaseModel(**my_dict)
        self.assertTrue(type(b.id) is str)
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

    def test_when_kwargs_passed_is_not_empty(self):
        """
        Checks that id, created_at and updated_at are created from kwargs
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        b = BaseModel(**my_dict)
        self.assertEqual(b.id, my_dict["id"])
        self.assertEqual(b.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(b.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
        When args and kwargs are passed, BaseModel should ignore args
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b = BaseModel("1234", id="234", created_at=dt_iso, name="Sonnie")
        self.assertEqual(b.id, "234")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.name, "Sonnie")

    def test_when_kwargs_passed_is_more_than_default(self):
        """
        Checks BaseModel does not break when kwargs contains more than
        the default attributes
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Firdaus"}
        b = BaseModel(**my_dict)
        self.assertTrue(hasattr(b, "name"))

    def test_new_method_not_called_when_dict_obj_is_passed_to_BaseModel(self):
        """
        Test that storage.new() is not called when a BaseModel obj is
        created from a dict object
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Sonnie"}
        b = BaseModel(**my_dict)
        self.assertTrue(b not in models.storage.all().values(),
                        "{}".format(models.storage.all().values()))
        del b

        b = BaseModel()
        self.assertTrue(b in models.storage.all().values())

    def test_that_save_method_updates_updated_at_attr(self):
        """
        Checks that save() method updates 'updated_at' attribute
        """
        b = BaseModel()
        sleep(0.02)
        temp_update = b.updated_at
        b.save()
        self.assertLess(temp_update, b.updated_at)

    def test_that_save_can_update_two_or_more_times(self):
        """
        Tests that the save method updates 'updated_at' two times
        """
        b = BaseModel()
        sleep(0.02)
        temp_update = b.updated_at
        b.save()
        sleep(0.02)
        temp1_update = b.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.01)
        b.save()
        self.assertLess(temp1_update, b.updated_at)

    def test_save_update_file(self):
        """
        Tests if file is updated when the 'save' is called
        """
        b = BaseModel()
        b.save()
        bid = "BaseModel.{}".format(b.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(bid, f.read())

    def test_that_to_dict_contains_correct_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        b_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, b_dict)

    def test_to_dict_contains_added_attributes(self):
        """
        Checks that new attributes are also returned by to_dict()
        """
        b = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        b.name = "Firdaus"
        b.email = "firduas@gmail.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, b.to_dict())

    def test_to_dict_output(self):
        """
        Checks the output returned by to_dict()
        """
        b = BaseModel()
        dt = datetime.now()
        b.id = "12345"
        b.created_at = b.updated_at = dt
        test_dict = {
            'id': "12345",
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dict, b.to_dict())

    def test_to_dict_with_args(self):
        """
        Checks that TypeError is returned when argument is passed to to_dict()
        """
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == "__main__":
    unittest.main()
