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
    def test_ids_is_unique(self):
    def test_type_of_id_is_str(self):
    def test_created_at_is_datetime(self):
    def test_updated_at_is_datetime(self):
    def test_two_models_different_created_at(self):
    def test_args_unused(self):
    def test_that_created_at_equals_updated_at_initially(self):
    def test_that_save_func_update_update_at_attr(self):
    def test_if_to_dict_returns_dict(self):
    def test_if_to_dict_returns_class_dunder_method(self):
    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
    def test_when_kwargs_passed_is_empty(self):
    def test_when_kwargs_passed_is_not_empty(self):
    def test_when_args_and_kwargs_are_passed(self):
    def test_when_kwargs_passed_is_more_than_default(self):
    def test_new_method_not_called_when_dict_obj_is_passed_to_BaseModel(self):
    def test_that_save_method_updates_updated_at_attr(self):
    def test_that_save_can_update_two_or_more_times(self):
    def test_save_update_file(self):
    def test_that_to_dict_contains_correct_keys(self):
    def test_to_dict_contains_added_attributes(self):
    def test_to_dict_output(self):
    def test_to_dict_with_args(self):
    def test_to_dict_not_dunder_dict(self):
if __name__ == "__main__":
    unittest.main()
