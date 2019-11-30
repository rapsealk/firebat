#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy

from firebase_admin import db
from firebase_app import FirebaseApplication


class FirebaseBridge:

    def __init__(self):
        self._data = {}
        db.reference("drone").listen(self.callback)

    @property
    def data(self):
        return self._data

    def callback(self, event):
        path = list(filter(lambda x: not not x, event.path.split('/')))
        data = self.to_dict(list(filter(lambda x: x is not None, \
                                        event.data))) if not path else event.data
        # print(event.event_type)
        print(path)
        print(data)

        try:
            key = path.pop()
            ref = self.data
            for p in path:
                ref = ref[p]
            ref[key] = data
        except IndexError:
            self._data = data

    @staticmethod
    def to_dict(list_):
        dict_ = {}
        for _, value in enumerate(list_):
            dict_[value["droneID"]] = value
        return dict_


if __name__ == "__main__":
    rospy.init_node("firebase_bridge", anonymous=True)
    FirebaseApplication.init()

    bridge = FirebaseBridge()
