#!/usr/bin/bash python3
"""
Test for file models/engine/file_storage.py
"""
from email.mime import base
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fs = FileStorage()
        cls.base_models = [BaseModel() for x in range(10)]
        cls.base_models[0].msg = "Hello world!!!"
        cls.base_models[9].msg = "Bye world!!!"

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.fs.file_path)

    def test_new(self):
        fs = self.__class__.fs
        base_models = self.__class__.base_models

        for model in self.base_models:
            fs.new(model)

        obj = fs.get_object
        self.assertEqual(len(obj), 10)
        self.assertEqual(
            obj.get(f"{base_models[0].__class__.__name__}.{base_models[0].id}").msg,
            "Hello world!!!",
        )
        self.assertEqual(
            obj.get(f"{base_models[9].__class__.__name__}.{base_models[9].id}").msg,
            "Bye world!!!",
        )

    def test_all(self):
        fs = self.__class__.fs
        base_models = self.__class__.base_models
        loop_count = 0
        for model in base_models:
            obj = fs.get_object.get(f"{model.__class__.__name__}.{model.id}")
            self.assertIsNotNone(obj)
            if loop_count == 0:
                self.assertEqual(obj.msg, "Hello world!!!")
            elif loop_count == 9:
                self.assertEqual(obj.msg, "Bye world!!!")

            loop_count += 1

    def test_save(self):
        fs = self.__class__.fs
        base_models = self.__class__.base_models

        fs.save()
        with open(fs.file_path) as json_file:
            dict_model = json.load(json_file)
            loop_count = 0
            for model in base_models:
                obj = dict_model.get(f"{model.__class__.__name__}.{model.id}")
                self.assertIsNotNone(obj)
                if loop_count == 0:
                    self.assertEqual(obj.get("msg"), "Hello world!!!")
                elif loop_count == 9:
                    self.assertEqual(obj.get("msg"), "Bye world!!!")

                loop_count += 1

    def test_reload(self):
        fs = self.__class__.fs
        base_models = self.__class__.base_models

        fs.reload()

        loop_count = 0
        for model in base_models:
            obj = fs.get_object.get(f"{model.__class__.__name__}.{model.id}")
            self.assertIsNotNone(obj)
            if loop_count == 0:
                self.assertEqual(obj.msg, "Hello world!!!")
            elif loop_count == 9:
                self.assertEqual(obj.msg, "Bye world!!!")

            loop_count += 1
