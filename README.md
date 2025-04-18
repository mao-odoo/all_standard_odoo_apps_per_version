# all_standard_odoo_apps_per_version


## OUR_MODULES_DIFF.json
A file listing all the names of standard Odoo apps introduced and removed in each version (community, design-themes, enterprise and industry).

Get it from your script at : https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/OUR_MODULES_DIFF.json

To get a full list of the modules per version:
```python
import json
from urllib.request import urlopen
OUR_MODULES_URL = "https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/OUR_MODULES_DIFF.json"

def only_num(version):
     return float(version.replace("saas~", ""))

def parse_diff(data):
    result = {}
    modules = set()
    for version, diff in sorted(data.items(), key=lambda x: only_num(x[0])):
        result[version] = modules = (modules - set(diff["-"])) | set(diff["+"])
    return result

with urlopen(OUR_MODULES_URL) as json_file:
    data = parse_diff(json.load(json_file))
```

## OUR_MODULES.json  (deprecated)
A file listing all the names of standard Odoo apps per version (community, design-themes, enterprise and inductry).
It has been replaced by OUR_MODULES_DIFF.json

> [!warning]
> This file has last been updated on 2025-04-18, will not be updated going forward and will be removed at the end of 2025

## is_my_module_standard

A basic script to check if a given list of modules are standard in version X.

run it without cloning this repo with:
```bash
python3 <(curl -s 'https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/is_my_module_standard.py') <version> -m <module_names>...
```

## new_app_per_version

A basic script to see apps introduced per version.

run it without cloning this repo with:
```bash
python3 <(curl -s 'https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/new_app_per_version.py')
```

# contribute

Open an issue called "I want to contribute" to potentially get a write access to this repository


# other similar projects

https://mrsweeter.github.io/glowing-modules/  is a web based project that lists the same information as this project, in a more human readable.
It even list older versions, and from which repository a module is coming from. Pretty Cool !
