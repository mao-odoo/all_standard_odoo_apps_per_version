#!/usr/bin/env python3
"""
Show the standard apps present in a version that did not exist in the previous one
"""
import json

def parse_version(version: str) -> float:
    return float(version.replace("saas~", ""))


def app():
    with open("OUR_MODULES_DIFF.json") as json_file:
        OUR_MODULES = json.load(json_file)

    return {
        version: mods["+"]
        for version, mods in sorted(OUR_MODULES.items(), key=lambda v: parse_version(v[0]))
    }


if __name__ == "__main__":
    for version, modules in app().items():
        print(version, ":")
        print(modules, "\n")
