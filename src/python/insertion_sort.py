#!/usr/bin/env python3
################################################################################
# insertion_sort.py
# SPDX-License-Identifier: GNU GPL v3.0
################################################################################
"""
Implement insertion sort algorithm to sort, in non-decreasing (ascending) or
non-increasing (descending) sort order an input stream of integers.
"""
import sys
import os
import random
import argparse

###############################################################################
# Global Variables: Used in multiple places. List here for documentation
###############################################################################

# Boolean globals for sorting order of a list's contents
SORT_ASC = True
SORT_DESC = False

# Boolean globals for checking a list's contents
IS_ASC = True
IS_DESC = False

# pylint: disable-msg=superfluous-parens
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
    parsed_args = parse_args(args)

    # Extract parsed cmdline flags into local variables
    verbose          = parsed_args.verbose
    do_debug         = parsed_args.debug_script
    dump_flag        = parsed_args.dump_flags

    if dump_flag:
        print(f'verbose = {verbose}')
        print(f'do_debug = {do_debug}')

    sys.exit(0)

###############################################################################
def insertion_sort(inplist:list, asc:bool = SORT_ASC) -> list:
    """Insertion sort algorithm"""
    if len(inplist) == 0:
        return []

    outlist = []
    ictr = 0
    while ictr < len(inplist):
        newval = inplist[ictr]
        outlist.append(newval)
        # No shuffling is needed for very 1st item inserted in outlist[]
        if ictr > 0:
            # Walk from end of the list, checking last item inserted with
            # prev items. Shuffle items to right as needed.
            jctr = ictr - 1     # Start from item prev-to newly inserted item
            while jctr >= 0:    # Walking backwards in already-sorted output items
                if (   (asc     and (outlist[jctr] > newval)) \
                    or (not asc and (outlist[jctr] < newval)) ):
                    tmpval = outlist[jctr]
                    outlist[jctr] = newval
                    outlist[jctr + 1] = tmpval
                    jctr -= 1
                else:
                    break
        ictr += 1

    return outlist

###############################################################################
def check_list(inplist: list, asc: bool = IS_ASC) -> bool:
    """Walk the input list and verify if items are in sorted order"""
    if len(inplist) == 0:
        return True

    ictr = 0
    while ictr < (len(inplist) - 1):
        if asc:
            if inplist[ictr] > inplist[ictr + 1]:
                return False
        else:
            if inplist[ictr] < inplist[ictr + 1]:
                return False
        ictr += 1
    return True

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
    parser  = argparse.ArgumentParser(description='Insertion Sort',
                                      formatter_class=argparse.RawDescriptionHelpFormatter)

    # Define arguments supported by this script
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
def test_basic():
    """ Run all the built-in basic unit-tests with small sorted data sets """
    assert check_list(insertion_sort([]))
    assert check_list(insertion_sort([1, 2, 3, 4, 5]))
    assert check_list(insertion_sort([3, 2, 1, 0 ]))

# -----
def test_basic_neg():
    """Simple negative tests to verify that check_list() is working right"""
    assert check_list(insertion_sort([1, 2, 3, 4, 5]), IS_DESC) is False
    assert check_list(insertion_sort([3, 2, 1, 0 ]), IS_DESC) is False
    assert check_list(insertion_sort([1, 2, 3, 4, 5], SORT_DESC), IS_ASC) is False
    assert check_list(insertion_sort([3, 2, 1, 0 ], SORT_DESC), IS_ASC) is False

# -----
def test_sort_asc():
    """Unit-tests to verify sorting in ascending order"""
    assert check_list(insertion_sort([4, 1, 5, 2, 65, -1]))

# -----
def test_sort_desc():
    """Unit-tests to verify sorting in descending order"""
    assert check_list(insertion_sort([4, 1, 5, 2, 65, -1], SORT_DESC), IS_DESC)

# -----
def test_sort_random_input():
    """
    Unit-tests to verify sorting of random set of data in asc/desc order
    Ref: https://docs.python.org/3/library/random.html
    """
    assert check_list(insertion_sort(random.sample(range(10000000), k=600)))
    assert check_list(insertion_sort(random.sample(range(10000000), k=600), SORT_DESC), IS_DESC)

# -----
def test_sort_random_input_with_neg_nos():
    """Unit-tests to verify sorting of random set of data in asc/desc order,
    from a data set including negative numbers
    """
    assert check_list(insertion_sort(random.sample(range(-10000000, 10000000), k=200)))
    assert check_list(insertion_sort(random.sample(range(-10000000, 10000000), k=2000),
                                     SORT_DESC), IS_DESC)

###############################################################################
# Start of the script: Execute only if run as a script
###############################################################################
if __name__ == "__main__":
    main()
