#!/usr/bin/env python3
"""
is_my_module_standard

usage:
    is_my_module_standard <version> -m <modules>...

"""
import json
import sys

DATA = "OUR_MODULES.json"


def parse_version(version: str) -> float:
    return float(version.replace("saas~", ""))


def app(target_version, modules):
    with open(DATA) as json_file:
        data = json.load(json_file)

    if target_version not in data:
        print(f"Version does not exists: {target_version}")
        print("Available versions:")
        for version in sorted(data.keys(), key=parse_version):
            print(f" - {version}")

        return

    standard_modules: set[str] = set()

    # Sort the versions and compute the list of modules
    # by adding new modules and removing old ones
    for version, mods in sorted(data.items(), key=lambda v: parse_version(v[0])):
        standard_modules = (standard_modules - set(mods["-"])) | set(mods["+"])
        if version == target_version:
            break

    standard_modules.add('studio_customization')
    s_modules = '\n'.join(m for m in modules if m in standard_modules)
    ns_modules = '\n'.join(m for m in modules if m not in standard_modules)
    print("\n\nStandard Modules:\n-----------------\n%s" % s_modules)
    print("\n\nThird-party Modules:\n---------------------\n%s" % ns_modules)


if __name__ == '__main__':
    args = sys.argv[1:]
    if "--help" in args or len(args) < 3 or args[1] != '-m':
        print(__doc__)
        sys.exit(0)
    version = args[0]
    version = version.replace("-", "~")
    modules = args[2:]
    app(version, modules)
