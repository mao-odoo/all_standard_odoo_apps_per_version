#!/usr/bin/env python3
"""
Show the standard apps present in a version that did not exist in the previous one
"""
import json

from urllib.request import urlopen

LOCAL_DATA = "OUR_MODULES_DIFF.json"
OUR_MODULES_URL = "https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/OUR_MODULES_DIFF.json"

def get_data_with_remote_fallback():
    """ get the LOCAL_DATA local file by default, but fall back to the remote file
    if the script is called as a stand alone script (if just this file was copied for example)"""
    try:
        with open(LOCAL_DATA) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        with urlopen(OUR_MODULES_URL) as json_file:
            return json.load(json_file)

def parse_version(version: str) -> float:
    return float(version.replace("saas~", ""))


def app():
    data = get_data_with_remote_fallback()
    return {
        version: mods["+"]
        for version, mods in sorted(data.items(), key=lambda v: parse_version(v[0]))
    }


if __name__ == "__main__":
    for version, modules in app().items():
        print(version, ":")
        print(modules, "\n")
