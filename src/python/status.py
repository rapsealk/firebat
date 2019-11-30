#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time

from firebase_admin import db
from firebase_app import FirebaseApplication


def callback(event):
    """
    --- Firebase Realtime Database Event ---
    event_type: put
    path: /1/timestamp
    data: 1575134531.1499143
    """
    print('--- Firebase Realtime Database Event ---')
    print('event_type:', event.event_type)
    print('path:', event.path)
    print('data:', event.data)


if __name__ == "__main__":
    FirebaseApplication.init()
    ref = db.reference("drone")
    drones = filter(lambda x: x is not None, ref.get())
    timestamp = time.time()
    status = map(lambda x: {
        "id": x["droneID"],
        "heartbeat": timestamp - x["timestamp"] < 5.0,
        "connected": x["connected"]
    }, drones)
    for stat in list(status):
        print(stat)

    ref.listen(callback)
