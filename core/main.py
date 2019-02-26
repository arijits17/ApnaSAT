import os
import sys
import argparse

import dimacs
import solver

def main(args):
    S = solver.Solver
    
    dimacs.parse(S, args.filename)
    
    S.solve()
    
    S.garbage_collect()

    

    

# ---------------------------------------------
# Function  :   running_options
# Action    :   Parses input options 
# ---------------------------------------------

def running_options():

    parser = argparse.ArgumentParser(description='Give DIMACS, take back SAT')
    parser.add_argument('filename', 
                        help='DIMACS Filename')

    args = parser.parse_args()
    
    return args


args = running_options()
main(args)