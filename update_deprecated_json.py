#!/usr/bin/env python3
"""
update_deprecated_json

update the content of the OUR_MODULES.json with the content of OUR_MODULES_DIFF.json
"""
import json
from collections import OrderedDict

DATA = "OUR_MODULES_DIFF.json"
DEPRECATED_DATA = "OUR_MODULES.json"

def only_num(version):
    return float(version.replace("saas~", ""))

def parse_diff(data):
    result = {}
    modules = set()
    for version, diff in sorted(data.items(), key=lambda x: only_num(x[0])):
        result[version] = modules = (modules - set(diff["-"])) | set(diff["+"])
    return result

with open(DATA) as json_file:
    data = parse_diff(json.load(json_file))

json_compat_data = OrderedDict()
for version in sorted(data.keys(), key=only_num):
    json_compat_data[version] = sorted(list(data[version]))

with open(DEPRECATED_DATA, 'w') as deprecated_file:
    json.dump(json_compat_data, deprecated_file, indent=4)
