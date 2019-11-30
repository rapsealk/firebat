#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from firebase_admin import db

import os
import sys
sys.path.append(os.path.abspath('../../src/python/'))

from firebase_app import FirebaseApplication


class FirebaseDatabaseTest(unittest.TestCase):

    def test_query(self):
        ref = db.reference("test/data")
        data = {
            "root": {
                "child": [
                    123,
                    "value4"
                ],
                "key": {
                    "value": 456
                }
            }
        }
        ref.set(data)
        self.assertEqual(data, ref.get())
        ref.delete()


if __name__ == "__main__":
    FirebaseApplication.init()
    unittest.main()
