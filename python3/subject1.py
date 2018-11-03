#!/usr/bin/env python3
import sys

num_genes = 0
len_genes = 0
with open(sys.argv[1], 'r') as f:
    for tmpline in f:
        if tmpline[0] == '#':
            continue
        itemlist = tmpline.rstrip().split('\t')
        if itemlist[2] == 'gene':
            num_genes += 1
            len_genes += int(itemlist[4]) - int(itemlist[3]) + 1

print(num_genes, len_genes)
