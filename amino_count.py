#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: dna2aa.py
Author: Stein Acker
Date: 16-10-2020

Description:
    When given a protein FASTA file, this program will calculate the raw 
    abundance of each amino acid in the FASTA file.

List of user-defined functions:
    fasta_to_line(fasta): When given a FASTA file in Python list format, this
    function returns a fully uppercase single-line string containing only the
    sequences.

List of non-standard modules:
    sys: Allows python script to easily interface with bash commands in a
    terminal.

Procedure:
    1. Create a list of single-letter amino acid codes.
    2. Iterate through the amino acid list and sum up the counts of these
    amino acids in the sequences.
    3. Subtract the sum of identified amino acids from the sum of total amino
    acids to identify number of 'X' amino acids.
    4. Return a text file containing the raw abundances of each amino acid.

Usage:
    ./amino_count.py fasta.faa output.txt
"""
import sys
import re
input_file = sys.argv[1]
output_file = sys.argv[2]
aminoacids = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S',
             'T','V','W','Y']

def fasta_to_line(fasta):
    all_amino = ''
    for line in fasta:
        if line.startswith('>') == False:
            line = line.strip('\n')
            all_amino += line
    all_amino = all_amino.upper()
    return all_amino

with open(input_file) as f:
    protein = fasta_to_line(f)

amino_counts = dict()

for amino in aminoacids:
    amino_counts[amino] = len(re.findall(amino, protein))
    
amino_counts['X'] = len(protein) - sum(amino_counts.values())

with open(output_file,'w') as o:
    for amino in aminoacids:
        o.write('{0} {1}\n'.format(amino, amino_counts[amino]))
    o.write('X ' + str(amino_counts['X']))
