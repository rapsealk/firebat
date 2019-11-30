#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

"""
Load configuration
"""
CONFIG_PATH = "../config/"


def config():
    config_file = open(CONFIG_PATH + "config.json", "r")
    config = config_file.readlines()
    config = json.loads(''.join(config))
    config["credentials"] = CONFIG_PATH + config["credentials"]
    config_file.close()
