#!/usr/bin/env python3
"""
Author : priamoskoumas <priamoskoumas@localhost>
Date   : 2023-01-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='World', help='Name to greet')
    return parser.parse_args()

  


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print('Hello, ' + args.name + '!')

    print(f'Hello, {args.name}!')  
# --------------------------------------------------
if __name__ == '__main__':
    main()
