# all_standard_odoo_apps_per_version


## OUR_MODULES_DIFF.json
A file listing all the names of standard Odoo apps introduced and removed in each version (community, design-themes, enterprise and inductry).

Get it from your script at : https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/OUR_MODULES_DIFF.json

## OUR_MODULES.json  (deprecated)
A file listing all the names of standard Odoo apps per version (community, design-themes, enterprise and inductry).
This file will soon stop being updated, and in the next few months will be removed from the repository.
It has been replaced by OUR_MODULES_DIFF.json

Get it from your script at : https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/OUR_MODULES.json

## is_my_module_standard

A basic script to check if a given list of modules are standard in version X.

run it without downloading this repo with:
```bash
python3 <(curl -s 'https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/is_my_module_standard.py') <version> -m <module_names>...
```

## new_app_per_version

A basic script to see apps introduced per version.

run it without downloading this repo with:
```bash
python3 <(curl -s 'https://raw.githubusercontent.com/mao-odoo/all_standard_odoo_apps_per_version/main/new_app_per_version.py')
```

# contribute

Open an issue called "I want to contribute" to potentially get a write access to this repository


# other related projects

https://mrsweeter.github.io/glowing-modules/  is a web based project that lists the same information as this project, in a more human readable.
It even list older versions, and from which repo is a module is comming from. Pretty Cool !
