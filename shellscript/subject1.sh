#!/bin/bash
awk -F "\t" '$3 == "gene" {num+=1 && sum+=$5-$4+1} END{print num,sum}' $1
