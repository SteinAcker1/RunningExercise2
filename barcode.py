#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: barcode.py
Author: Stein Acker
Date: 16-10-2020

Description:
    When given a multi FASTQ file, this program will filter the sequences into 
    4 new multi FASTQ files based on whether they contain the barcode TATCCTCT,
    GTAAGGAG, TCTCTCCG, or no barcode at all.

List of user-defined functions:
    none

List of non-standard modules:
    sys: Allows python script to easily interface with bash commands in a
    terminal.

Procedure:
    1. Generate a list of FASTQ data tuples in list format.
    2. Separate these sequences into their respective FASTQ files based on 
    barcode.

Usage:
    ./barcode.py input.fastq output1.fastq output2.fastq output3.fastq output_undefined.fastq
"""
#%% Setup

import sys
fastq = sys.argv[1]
sample1 = sys.argv[2]
sample2 = sys.argv[3]
sample3 = sys.argv[4]
undef = sys.argv[5]

#%% Step 1: Generate a list of FASTQ data tuples in list format.

newFastq = []
with open(fastq,'r') as f:
    for line in f:
        #If the line marks the start of a header...
        if line.startswith('@'):
            #Save that line and each of the next 3 lines as strings and add 
            #them to the newFastq list as a tuple.
            sequence = next(f)
            plus = next(f)
            quality = next(f)
            #This conditional eliminates the risk of the program finding an @
            #used as a quality marker and mistaking it for a new header.
            if plus == '+\n': 
                newFastq.append((line,sequence,plus,quality))
            
#%% Step 2: Separate these sequences into their respective FASTQ files.

with open(sample1, 'w') as s1, open(sample2, 'w') as s2, open(sample3, 'w') as s3, open(undef, 'w') as u:
    for line in newFastq:
        #For each piece of FASTQ data, the program checks if the barcode shows
        #up at the start of the sequence (the 2nd part of each list) and, if 
        #a barcode is found, the FASTQ data are sorted into the proper file.
        #If no barcode is found, then the data are sorted into the 
        #"undefined" file.
        if line[1].startswith('TATCCTCT'):
            s1.write(line[0]+line[1]+line[2]+line[3])
        elif line[1].startswith('GTAAGGAG'):
            s2.write(line[0]+line[1]+line[2]+line[3])
        elif line[1].startswith('TCTCTCCG'):
            s3.write(line[0]+line[1]+line[2]+line[3])
        else:
            u.write(line[0]+line[1]+line[2]+line[3])