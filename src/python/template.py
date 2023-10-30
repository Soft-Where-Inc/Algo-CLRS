#!/usr/bin/env python3
################################################################################
# template.py
# SPDX-License-Identifier: GNU GPL v3.0
################################################################################
"""
Script to go through and implement some processing. Describe the workings.
"""
import sys
import os
import argparse
import tempfile

###############################################################################
# Global Variables: Used in multiple places. List here for documentation
###############################################################################

THIS_SCRIPT          = os.path.basename(__file__)
THIS_PKGSRC_DIR      = os.path.dirname(THIS_SCRIPT)

###############################################################################
# main() driver
###############################################################################
def main():
    """
    Shell to call do_main() with command-line arguments.
    """
    do_main(sys.argv[1:])

###############################################################################
def do_main(args) -> (bool, int, int, str):
    """
    Main driver to implement argument processing.
    """
    if len(args) == 0:
        print(f"Usage: {sys.argv[0]}  <root src-dir>")
        print(f"Example: {sys.argv[0]} $HOME/Code/myProject/")
        sys.exit(0)

    # By default, all files will be generated in /tmp first.
    tmp_dir = tempfile.gettempdir() + '/'

    parsed_args = parse_args(args)

    # Extract parsed cmdline flags into local variables
    src_root_dir     = parsed_args.src_root_dirname
    inc_dirname      = tmp_dir if parsed_args.inc_dirname is None else parsed_args.inc_dirname
    src_dirname      = tmp_dir if parsed_args.src_dirname is None else parsed_args.src_dirname
    verbose          = parsed_args.verbose
    do_debug         = parsed_args.debug_script
    dump_flag        = parsed_args.dump_flags

    if dump_flag:
        print(f'src_root_dir = {src_root_dir}')
        print(f'inc_dirname = {inc_dirname}')
        print(f'src_dirname = {src_dirname}')
        print(f'verbose = {verbose}')
        print(f'do_debug = {do_debug}')

    sys.exit(0)

###############################################################################
# Argument Parsing routine
def parse_args(args):
    """
    Command-line argument parser.

    For how-to re-work argument parsing so it's testable.
    """
    # pylint: disable-msg=line-too-long
    # Ref: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
    # pylint: enable-msg=line-too-long

    # ---------------------------------------------------------------
    # Start of argument parser, with inline examples text
    # Create 'parser' as object of type ArgumentParser
    parser  = argparse.ArgumentParser(description='FIXME - Describe your tool / script here.',
                                      formatter_class=argparse.RawDescriptionHelpFormatter,
                                      epilog=r'''Examples:

- Basic usage:
    ''' + THIS_SCRIPT + ''' --src-root-dir < source code root-dir >
''')

    # Define arguments supported by this script
    parser.add_argument('--fixme-root-dir', dest='root_dirname'
                        , metavar='<src-root-dir>'
                        , required=True
                        , default=THIS_PKGSRC_DIR
                        , help=r'''Source root dir name, default: ''' + THIS_PKGSRC_DIR)

    parser.add_argument('--fixme-includes-dir', dest='inc_dirname'
                        , metavar='<include-files-dir>'
                        , default=None
                        , help='Include .h files dir name.' + ' default: ' + THIS_PKGSRC_DIR)

    parser.add_argument('--fixme-source-dir', dest='src_dirname'
                        , metavar='<source-files-dir>'
                        , default=None
                        , help='Source files dir name, default: ' + THIS_PKGSRC_DIR)

    # ======================================================================
    # Debugging support
    parser.add_argument('--verbose', dest='verbose'
                        , action='store_true'
                        , default=False
                        , help='Show verbose progress messages')

    parser.add_argument('--debug', dest='debug_script'
                        , action='store_true'
                        , default=False
                        , help='Turn on debugging for script\'s execution')

    parser.add_argument('--dump-data', dest='dump_flags'
                        , action='store_true'
                        , default=False
                        , help='Dump args, other data for debugging')

    parsed_args = parser.parse_args(args)

    if parsed_args is False:
        parser.print_help()

    return parsed_args

###############################################################################
# Start of the script: Execute only if run as a script
###############################################################################
if __name__ == "__main__":
    main()
