#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import configparser

def main():
    """Generate a Python script with a main, shebang, etc."""
    init_python()

def init_python():
    """Generate a Python script with a main, shebang, etc."""
    args = argparser()

    cwd = os.getcwd()
    fname = args.fname if args.fname.endswith(".py") else args.fname+".py"
    if os.path.isfile(os.path.join(cwd, fname)):
        msg = f"'{fname}' already exists!"
        raise FileExistsError(msg)

    ## make a config parser
    ## then update the default dict with the argparser arguments
    with open(os.path.join(cwd, fname), "w") as f:
        for line in file_input(args):
            f.write(line.replace("\t", 4*" ") + "\n")

def configparser():
    """Config file parser to read deafault settings

    The config file can be created by the user to 
    change default arguments of the file creation 
    function.
    """
    parser = configparser.ConfigParser()
    config_file = None
    ## expand the search options for the config file later
    ## keep the list in the priority order
    config_locs = [os.curdir, os.path.expanduser('~')] 
    for loc in config_locs:
        if os.path.exists(os.path.join(loc, 'scripts_config.cf')):
            config_file = os.path.join(loc, 'scripts_config.cf')
            break
        else:
            pass
    
    if config_file is not None:
        parser.read(config_file)
        return parser
    else:
        return
            
def argparser():
    """Argument parser to allow for a flexible usage of the script."""
    description = "A script used to generate Python files."
    parser = argparse.ArgumentParser(description=description)
    
    fname = ("Name of the file to be created (with or without '.py' "
             + "extension).")
    parser.add_argument("fname", metavar="file name", type=str, 
                        help=fname)

    author = "Add an author (default: Max Schalz)."
    parser.add_argument("--author", type=str, default="Max Schalz", 
                        help=author)
    license_ = "Add a license (default: BSD-3-Clause)."
    parser.add_argument("--license", type=str, default="BSD-3-Clause",
                        help=license_)
    main_ = "If used, do *not* add a main function and a boilerplate."
    parser.add_argument("--main", action="store_false", help=main_)

    # Add imports.
    ap = "Add an argument parser."
    parser.add_argument("--ap", action="store_true", help=ap)
    np = "Add numpy import."
    parser.add_argument("--np", action="store_true", help=np)
    os = "Add os import"
    parser.add_argument("--os", action="store_true", help=os)
    pd = "Add pandas import."
    parser.add_argument("--pd", action="store_true", help=pd)
    plt = "Add matplotlib.pyplot import."
    parser.add_argument("--plt", action="store_true", help=plt)

    return parser.parse_args()

def file_input(args):
    """Generate the file input."""
    lines = []

    # Only add a \n to the end of the string if there should be one 
    # empty line in the output.
    ap_call = '\targs = argparser()'
    ap_func = ('def argparser():\n'
               '\tdescription = "An argument parser"\n'
               '\tparser = argparse.ArgumentParser(description=description)\n\n'
               '\tparser.add_argument("-a", "--long", help="")\n\n'
               '\treturn parser.parse_args()')

    author = f'__author__ = "{args.author}"'
    boilerplate = 'if __name__=="__main__":\n\tmain()'
    license_ = f'__license__ = "{args.license}"\n'
    main_ = 'def main():\n\t"""Main function."""'
    shebang = '#!/usr/bin/env python3'
    encoding = '# -*- coding: utf-8 -*-\n'

    # Imports
    ap = 'import argparse'
    np = 'import numpy as np'
    os = 'import os'
    pd = 'import pandas as pd'
    plt = 'import matplotlib.pyplot as plt'

    lines.append(shebang)
    lines.append(encoding)

    lines.append(author)
    lines.append(license_)

    if args.ap:
        lines.append(ap)
    if args.plt:
        lines.append(plt)
    if args.np:
        lines.append(np)
    if args.os:
        lines.append(os)
    if args.pd:
        lines.append(pd)
    lines.append("\n")

    lines.append(main_)
    if args.ap:
        lines.append(ap_call)
    lines.append("\n")

    if args.ap:
        lines.append(ap_func)
        lines.append("\n")

    lines.append(boilerplate)

    return lines

if __name__=="__main__":
    main()
