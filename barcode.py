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
        if line.startswith('@'):
            sequence = next(f)
            plus = next(f)
            quality = next(f)
            newFastq.append((line,sequence,plus,quality))
            
#%% Step 2: Separate these sequences into their respective FASTQ files.

with open(sample1, 'w') as s1, open(sample2, 'w') as s2, open(sample3, 'w') as s3, open(undef, 'w') as u:
    for line in newFastq:
        if line[1].startswith('TATCCTCT'):
            s1.write(line[0]+line[1]+line[2]+line[3])
        elif line[1].startswith('GTAAGGAG'):
            s2.write(line[0]+line[1]+line[2]+line[3])
        elif line[1].startswith('TCTCTCCG'):
            s3.write(line[0]+line[1]+line[2]+line[3])
        else:
            u.write(line[0]+line[1]+line[2]+line[3])