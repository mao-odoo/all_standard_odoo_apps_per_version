#!/usr/bin/env python3
"""
is_my_module_standard

usage:
    is_my_module_standard <version> -m <modules>...

"""
import json
import sys

DATA = "OUR_MODULES.json"

def app(version, modules):
    with open(DATA) as json_file:
        data = json.load(json_file)
    standard_modules = set(data[version])
    s_modules = '\n'.join(m for m in modules if m in standard_modules)
    ns_modules = '\n'.join(m for m in modules if m not in standard_modules)
    print("\n\nStandard Modules:\n-----------------\n%s" % s_modules)
    print("\n\nNon Standard Modules:\n---------------------\n%s" % ns_modules)


if __name__ == '__main__':
    args = sys.argv[1:]
    if "--help" in args or len(args) < 3 or args[1] != '-m':
        print(__doc__)
        sys.exit(0)
    version = args[0]
    modules = args[2:]
    app(version, modules)
