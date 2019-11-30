#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import firebase_admin
from firebase_admin import credentials

"""
Load configuration
"""
CONFIG_PATH = "../../config/"
config_file = open(CONFIG_PATH + "config.json", "r")
config = config_file.readlines()
config = json.loads(''.join(config))
config["credentials"] = CONFIG_PATH + config["credentials"]
config_file.close()


def GOOGLE_APPLICATION_CREDENTIALS():
    return config["credentials"]


class FirebaseApplication:

    @staticmethod
    def init(cert_path=None):
        cert_path = cert_path if cert_path is not None \
            else GOOGLE_APPLICATION_CREDENTIALS()
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate(cert_path)
        # Initialize the app with a service account, granting admin privileges
        default_app = firebase_admin.initialize_app(cred, {
            "databaseURL": config["databaseURL"]
        })
        print(default_app.name)


if __name__ == "__main__":
    pass
