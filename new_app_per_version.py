#!/usr/bin/env python3
"""
Show the standard apps present in a version that did not exist in the previous one
"""
import json
import sys

# a sorted list of the versions
# (in git branch format)
VERSIONS = [
    "saas-15.2",
    "saas-15.1",
    "15.0",
    "14.0",
    "13.0",
    "saas-12.3",
    "12.0",
    "saas-11.3",
    "11.0",
    "saas-15",
    "saas-14",
    "10.0",
    "saas-11",
    "saas-10",
    "9.0",
    "saas-6",
    "8.0",
]

SPECIAL_CASES = {
    "saas-15": "10.saas-15",
    "saas-14": "10.saas-14",
    "saas-11": "9.saas-11",
    "saas-10": "9.saas-10",
    "saas-6": "8.saas-6",
    "saas-3": "7.saas-3",
}

def _fmt_version(version):
    return SPECIAL_CASES.get(version, version).replace("-", "~")

# a sorted list of the versions
# (in "internal" format)
VERSIONS = [_fmt_version(v) for v in VERSIONS]


def app():
    with open("OUR_MODULES.json") as json_file:
        OUR_MODULES = json.load(json_file)
    res = dict()
    for vA, vB in zip(VERSIONS, VERSIONS[1:]):
        res[f"{vA} - {vB}"] = [m for m in OUR_MODULES[vA] if m not in OUR_MODULES[vB]]
    return res

if __name__ == "__main__":
    for diff, modules in app().items():
        print(diff, ":")
        print(modules)
        print("\n"*5)