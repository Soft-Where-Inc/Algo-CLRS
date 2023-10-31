#!/usr/bin/env python3
################################################################################
# ex1_1_comparison_of_running_times.py:
# SPDX-License-Identifier: GNU GPL v3.0
################################################################################
"""
Script to do some relative computations for different O(n) algorithms.

For each function f(n) and time t (in the following table), determine the
largest size 'n' of a data set that can be solved in time 't', assuming
that the algorithm to solve the problem takes f(n) microseconds (us).

Ref: CLRS Pg. 13, Ex 1-1.
     https://walkccc.me/CLRS/Chap01/Problems/1-1/
"""
import sys
import os
import argparse
from math import log

# pylint: disable-msg=superfluous-parens

###############################################################################
# Global Variables: Used in multiple places. List here for documentation
###############################################################################

THIS_SCRIPT          = os.path.basename(__file__)
THIS_PKGSRC_DIR      = os.path.dirname(THIS_SCRIPT)

# Time unit conversion factors
NMILLIS_PER_SEC = 1000
NMICROS_PER_SEC = (NMILLIS_PER_SEC * 1000)

# Other conversion constants
K_KILO = 1024
K_MEGA = (K_KILO * 1024)
K_GIGA = (K_MEGA * 1024)
K_TERA = (K_GIGA * 1024)
K_PETA = (K_TERA * 1024)

# Stringify K-constants via hash lookup
K_Names = {  K_KILO : "KiB"
           , K_MEGA : "MiB"
           , K_GIGA : "GiB"
           , K_TERA : "TiB"
           , K_PETA : "PiB"
          }

# Names of O(n) functions to evaluate
O_LOG_N     = 'log-n'
O_SQRT_N    = 'sqroot-n'
O_N         = 'n'
O_N_LOG_N   = 'n-log-n'
O_N_SQUARED = 'n-squared'
O_N_CUBED   = 'n-cubed'
O_2_POWER_N = '2-power-of-n'
O_N_FACT    = 'n-factorial'
POWERS_OF_2 = 'print-powers-of-2'

# Array of O(n) functions that we know about
O_fn_names = [  O_LOG_N
              , O_SQRT_N
              # We can deal with 'n' for 1 sec, only for these algorithms
              , O_N
              , O_N_LOG_N
              , O_N_SQUARED
              , O_N_CUBED
              , O_2_POWER_N
              , O_N_FACT
              , POWERS_OF_2
             ]

###############################################################################
def o_log_n(num_secs:int, do_debug:bool) -> int:
    """
    Evaluate max-n for O(lgn) run-time that can be computed in num_secs seconds
    """
    # print("Evaluate O(log n)", a_variable)
    num_us = (num_secs * NMICROS_PER_SEC)
    base2 = 2
    expected = base2 ** num_us
    print(f'Expected result: {expected}')

    num_n = 1
    while log(num_n, base2) < num_us:
        num_n = num_n + 100000
        # if num_n % 1000 == 0:
        if do_debug:
            log2_value = log(num_n, base2)
            print(f'Value of log2 of {num_n} is {log2_value}')

    result = num_n - 1
    print(f'Result: {result}')

###############################################################################
def o_n_log_n(num_secs:int, do_debug:bool) -> int:
    """
    Evaluate max-n for O(nlgn) run-time that can be computed in num_secs seconds
    """
    num_us = (num_secs * NMICROS_PER_SEC)
    base2 = 2
    num_n = 1
    while True:
        est_us = num_n * log(num_n, base2)
        if est_us == num_us:
            result = num_n
            break
        if est_us > num_us:
            result = num_n - 1
            break

        if (num_n % 1000 == 0) and do_debug:
            print(f'Estimated time for n={num_n} = {est_us}')
        num_n = num_n + 1

    print(f'Evaluate O(nlog n) for {num_secs} seconds, Result: {result}')

###############################################################################
def o_n_squared(num_secs:int, do_debug:bool) -> int:
    """
    Evaluate max-n for O(n^2) run-time that can be computed in num_secs seconds
    """
    num_us = (num_secs * NMICROS_PER_SEC)
    num_n = 1
    while True:
        est_us = num_n ** 2
        if est_us == num_us:
            result = num_n
            break
        if est_us > num_us:
            result = num_n - 1
            break

        if (num_n % 1000 == 0) and do_debug:
            print(f'Estimated time for n={num_n} = {est_us}')
        num_n = num_n + 1

    print(f'Evaluate O(n^2) for {num_secs} seconds, Result: {result}')

###############################################################################
def o_n_cubed(num_secs:int, do_debug:bool) -> int:
    """
    Evaluate max-n for O(n^3) run-time that can be computed in num_secs seconds
    """
    num_us = (num_secs * NMICROS_PER_SEC)
    num_n = 1
    while True:
        est_us = num_n ** 3
        if est_us == num_us:
            result = num_n
            break
        if est_us > num_us:
            result = num_n - 1
            break

        if (num_n % 1000 == 0) and do_debug:
            print(f'Estimated time for n={num_n} = {est_us}')
        num_n = num_n + 1

    print(f'Evaluate O(n^3) for {num_secs} seconds, Result: {result}')

###############################################################################
def o_2_power_n(num_secs:int, do_debug:bool) -> int:
    """
    Evaluate max-n for O(2^n) run-time that can be computed in num_secs seconds
    """
    num_us = (num_secs * NMICROS_PER_SEC)
    num_n = 1
    while True:
        est_us = (2 ** num_n)
        if est_us == num_us:
            result = num_n
            break
        if est_us > num_us:
            result = num_n - 1
            break

        if (num_n % 1000 == 0) and do_debug:
            print(f'Estimated time for n={num_n} = {est_us}')
        num_n = num_n + 1

    print(f'Evaluate O(2^n) for {num_secs} seconds, Result: {result}')

###############################################################################
def print_powers_of_2(max_n:int, do_debug:bool) -> int:
    """Print powers of 2, from 1 .. max_n"""
    if do_debug:
        print(f'Print powers of 2 from 1..{max_n}')

    ictr = 0
    print(f'{"ictr":>5} {"2^ictr":>22}')
    print(f'{"-----":>5} {"------":>22}')
    while ictr <= max_n:
        result = 2 ** ictr
        result_str = xform_num_to_str(result)

        print(f'{ictr:>4}   {result:>20d} {result_str}')
        ictr = ictr + 1

# Hash of method implementing O(function) to compute 'n', given time_s
O_fn_methods = {  O_N_LOG_N     : o_n_log_n
                , O_N_SQUARED   : o_n_squared
                , O_N_CUBED     : o_n_cubed
                , O_2_POWER_N   : o_2_power_n
                , POWERS_OF_2   : print_powers_of_2
               }

###############################################################################
def xform_num_to_str(num:int) -> str:
    """Convert power-of-2 number to its string name, from lookup hash."""
    if num < K_KILO:
        return ""

    if num >= K_PETA:
        num_str = str(num / K_PETA)
        num_k_name = K_Names[K_PETA]
    elif num >= K_TERA:
        num_str = str(num / K_TERA)
        num_k_name = K_Names[K_TERA]
    elif num >= K_GIGA:
        num_str = str(num / K_GIGA)
        num_k_name = K_Names[K_GIGA]
    elif num >= K_MEGA:
        num_str = str(num / K_MEGA)
        num_k_name = K_Names[K_MEGA]
    elif num >= K_KILO:
        num_str = str(num / K_KILO)
        num_k_name = K_Names[K_KILO]

    # Form the result string from constituent parts
    # Auto-format string'fied version of number w/units to align to field
    num_str_af = f'{num_str.split(".", maxsplit=1)[0]:>6}'
    return '(' + num_str_af + ' ' + num_k_name + ')'

###############################################################################
# main() driver
###############################################################################
def main():
    """
    Shell to call do_main() with command-line arguments.
    """
    do_main(sys.argv[1:])

###############################################################################
def do_main(args):
    """
    Main driver to implement argument processing.
    """
    if len(args) == 0:
        print(f'Usage: {sys.argv[0]}  --help')
        sys.exit(0)

    parsed_args = parse_args(args)

    # Extract parsed cmdline flags into local variables
    oh_of_n     = parsed_args.oh_of_n
    list_algs   = parsed_args.list_algs
    num_secs    = int(parsed_args.time_s)
    max_n       = int(parsed_args.max_n)
    verbose     = parsed_args.verbose
    do_debug    = parsed_args.debug_script
    dump_flag   = parsed_args.dump_flags

    if dump_flag:
        print(f'oh_of_n = {oh_of_n}')
        print(f'verbose = {verbose}')
        print(f'do_debug = {do_debug}')

    if list_algs:
        pr_list(O_fn_names, 'List of O(n) function names to be analyzed:')
        sys.exit(0)

    if oh_of_n not in O_fn_methods:
        print(f'Error: Unsupported O(n) function \'{oh_of_n}\'.'
               + ' Use --list argument for supported O(n) function names.')
        sys.exit(1)

    # Dispatch the method implementing the O(n) strategy
    if oh_of_n in O_fn_methods:
        O_fn_methods[oh_of_n]((max_n if oh_of_n == POWERS_OF_2 else num_secs),
                              do_debug)
    else:
        print(f'Error: Unimplemented O(n) function for \'{oh_of_n}\'.'
               + ' Use --list argument for implemented O(n) method names.')
        sys.exit(1)

    sys.exit(0)

###############################################################################
# Argument Parsing routine
def parse_args(args):
    """
    Command-line argument parser.

    For how-to re-work argument parsing so it's testable.
    """
    # pylint: disable-next=line-too-long
    # Ref: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module

    # ---------------------------------------------------------------
    # Start of argument parser, with inline examples text
    # Create 'parser' as object of type ArgumentParser
    parser  = argparse.ArgumentParser(description='FIXME - Describe your tool / script here.',
                                      formatter_class=argparse.RawDescriptionHelpFormatter,
                                      epilog=f'''Examples:

- Basic usage:
    {THIS_SCRIPT} --list
    {THIS_SCRIPT} --oh-of-n={O_fn_names[0]} ''')

    # Define arguments supported by this script
    parser.add_argument('--list-args', dest='list_algs'
                        , action='store_true'
                        , default=False
                        , help='List names of O(n) functions to be tested')

    parser.add_argument('--oh-of-n', dest='oh_of_n'
                        , metavar='<string>'
                        , default=O_fn_names[0]
                        , help='Name O(n) function name to evaluate')

    parser.add_argument('--max-n', dest='max_n'
                        , metavar='<number>'
                        , default=10
                        , help='Max-value-of-n to print powers-of-2')

    parser.add_argument('--time-s', dest='time_s'
                        , metavar='<number>'
                        , default=1
                        , help='Time, in seconds.')

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
# Helper methods
###############################################################################

def pr_list(an_array:list, header=None):
    """Print the contents of an array."""
    if header is not None:
        print(header)

    for item in (an_array):
        print(' ', item)

###############################################################################
# Start of the script: Execute only if run as a script
###############################################################################
if __name__ == "__main__":
    main()
