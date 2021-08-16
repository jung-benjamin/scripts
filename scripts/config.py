#! /usr/bin/env python3

"""Configuration options for initlatex and initpython

Commandline options
-------------------
--template, -t
    specify a section of the configfile to use for copying the template


Configfile options
------------------
"""

import os
import argparse
import configparser

CONFIG_FNAME = 'scripts_config.cfg'
CONFIG_LOCS = [os.curdir, os.path.expanduser('~')] 


def parse_config(args):
    """Config file parser to read deafault settings

    The config file can be created by the user to 
    change default arguments of the file creation 
    function.
    """
    parser = configparser.ConfigParser()
    config_file = None
    ## expand the search options for the config file later
    ## keep the list in the priority order
    config_locs = [args.dirname] + CONFIG_LOCS
    for loc in config_locs:
        if os.path.exists(os.path.join(loc, CONFIG_FNAME)):
            config_file = os.path.join(loc, CONFIG_FNAME)
            break
        else:
            pass
    
    if config_file is not None:
        parser.read(config_file)
        return parser
    else:
        return

def argparser():
    """Argument parser."""
    description = "Initialise the main files needed in a LaTeX article."
    parser = argparse.ArgumentParser(description=description)

    dirname = ("Name of the directory in which the LaTeX files will be"
               + " generated into.")
    parser.add_argument("dirname", metavar="directory name", type=str,
                        help=dirname)
    
    current_dir = ("If this flag is set, the files are generated into "
                   "the current working directory.")
    parser.add_argument("--current_dir", action="store_true",
                        help=current_dir)
    
    # Document-specific stuff.
    author = "Author of the LaTeX article."
    parser.add_argument("--author", type=str, default="Max Schalz",
                        help=author)
    title = "Title of the LaTeX article."
    parser.add_argument("--title", type=str, default="Document",
                        help=title)
    bib = "If this flag is set, a biblatex bibliography is added."
    parser.add_argument("--bib", action="store_true", help=bib)

    no_toc = "If this flag is set, do not include a table of contents."
    parser.add_argument("--no_toc", action="store_true", help=no_toc)

    template_path = "Path to a directory containing template files."
    parser.add_argument("--template_path", type = str)

    return parser.parse_args()

