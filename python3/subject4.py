#!/usr/bin/env python3
import sys
from functools import total_ordering


@total_ordering
class EcNumber:
    def __init__(self, ec_num_str):
        self.__ec_number = tuple(map(int, ec_num_str.split(':')[1].split('.')))

    def __lt__(self, other):
        return self.__ec_number < other.__ec_number
    
    def __eq__(self, other):
        return self.__ec_number == other.__ec_number
    
    def __str__(self):
        return 'ec:{}.{}.{}.{}'.format(*(self.__ec_number))


def main():
    
    enzyme_list = []
    with open(sys.argv[1], 'r') as f:
        for tmpline in f:
            ec_num_str, description = tmpline.rstrip().split('\t')
            enzyme_list.append((EcNumber(ec_num_str), description))

    for ec_number, description in sorted(enzyme_list):
        print('{}\t{}'.format(ec_number, description))


if __name__ == '__main__':
    main()
    
