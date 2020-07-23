# Special thanks:
#
# Manjeet Singh for his lambda way to sort list of dicts by their values
# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
# https://www.linkedin.com/in/manjeet04/
# https://github.com/manjeet04
#

import os
import webbrowser
import shutil
import json
import time

class Kaufer(object):
    def __init__(self):
        self._config_filename = "stores.json"
        self.stores = None

        if not os.path.isfile(self._config_filename):
            self._create_default_config()

        self._read_config()

    def _create_default_config(self):
        shutil.copyfile("default/%s" % self._config_filename,
                            self._config_filename)

    def _read_config(self):
        file = open(self._config_filename, "r")
        unsorted_stores = json.load(file)

        self.stores = sorted(unsorted_stores,
                            key=lambda i: i["name"].lower())
        file.close()

    def save_config(self):
        file = open(self._config_filename, "w")
        json.dump(self.stores, file, indent=4)
        file.close()

    def search(self, query):
        print("Using stores: ")
        for store in self.stores:
            if store["enabled"]:
                print("%s" % store["name"], end=" ")
                l = store["link"].replace("{{ query }}", query)
                time.sleep(0.5)
                webbrowser.open(l)

        print("")